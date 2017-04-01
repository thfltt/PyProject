# -*- coding: utf-8 -*-
'''
Created on 2017年3月25日

@author: hc
'''

import time
import pdb
import pexpect
from pexpect import pxssh

#from com.whaley.exception.SSHExecption import SSHException,TimeOutExecption
class SSHException(Exception):
    def __init__(self,host):
        self.host = host
    
    def __str__(self):
        return "Error  when try to connect with %s" %self.host

class TimeOutExecption(Exception):
    def __init__(self,command,output):
        self.command = command
        self.output = output
    def __str__(self): 
        return "Timout on %s !" %self.command
    def get_output(self):
        return self.output

class SSHUtils():
    def __init__(self,host,username,password):
        self.magic_prompt="MAGIC PROMPT"
        try:
            self.session=pxssh.pxssh()
            self.host = host
            self.username = username
            self.password= password
            if ":" in host:
                self.ip= host.split(":")[0]
                self.port = int(host.split(":")[1])
                self.session.login(self.ip,self.username,self.password,original_prompt='[$#>]',port=self.port,login_timeout=20)
            else:
                self.session.login(self.host,self.username,self.password,original_prompt='[$#>]')
            #self.send_expect('stty -echo','# ',timeout=10)
        except Exception,e:
            print str(e)
            raise SSHException(self.host)
    def send_expect_base(self,command,expected,timeout):
        self.clean_session()
        #self.session.PROMPT = expected
        self.__sendline(command)
        self.__prompt(command, timeout)
        before = self.get_out_before()
        return before
    
    def send_expect(self,command,expected,timeout=15,verify=False):
        ret = self.send_expect_base(command, expected, timeout)
        if verify:
            ret_status = self.send_expect_base("echo $?", expected, timeout)
            if not int(ret_status):
                return ret
            else:
                print "Command:%s executed failed!" %command
                return int(ret_status)
        else:
            return ret
        
        
            
    
    def get_session_before(self,timeout=15):
        """
        get all output before timeout
        """
        #self.session.PROMPT = self.magic_prompt
        try:
            self.session.prompt(timeout)
        except Exception as e:
            print e 
            pass
        before = self.get_out_before()
        self.__flush()
        return before
    def clean_session(self):
        self.get_session_before(timeout=0.01)
    def __flush(self):
        """
        clear the session buffer
        """
        self.session.buffer=''
        self.session.before=''
        
    def __prompt(self,command,timeout):
        if not self.session.prompt(timeout):
            raise TimeOutExecption(command,self.get_out_all())
        
    def __sendline(self,command):
        if not self.isalive():
            raise SSHException(self.host)
        if len(command)==2 and command.startwith('^'):
            self.session.sendcontrol(command[1])
        else:
            self.session.sendline(command)
    
    def get_out_before(self):
        if not self.isalive():
            raise SSHException(self.host)
        self.session.flush()
        before = self.session.before.rsplit("\r\n",1)
        if before[0] == "[PEXPECT]":
            before[0] = ''
        return before[0]
        
    def get_out_all(self):
        self.session.flush()
        output = self.session.before
        output.replace("[PEXPECT]", "")
        return output
    def isalive(self):
        return self.session.isalive()
    def copy_file_from(self,src,dst=".",password=''):
        """
        copy file from remote to local, the local dest folder is currently working folder
        """
        command = 'scp -v {0}@{1}:{2} {3}'.format(self.username,self.host,src,dst)
        if ':' in self.host:
            command = 'scp -v -P {0} -o NoHostAuthenticationForLocalhost=yes {1} {2}@{3}:{4}'.format(
            str(self.port),self.username,self.ip,src,dst)
        if password=='':
            self.__spawn_scp(command, self.password)
        else:
            self.__spawn_scp(command, password)
            
        
    def copy_file_to(self,src,dst="~/" ,password=''):
        """
        copy local file to remote , the dest  default folder is the login user's home
        """
        command = 'scp -v {0} {1}@{2} {3}'.format(src,self.username,self.host,dst)
        if ':' in self.host:
            command='scp -v -P {0} -o NoHostAuthenticationForLocalhost=yes {1} {2}@{3}:{4}'.format(
            str(self.port),src,self.username,self.ip ,dst)
        if password=='':
            self.__spawn_scp(command, self.password)
        else:
            self.__spawn_scp(command, password)
            
    def __spawn_scp(self,scp_cmd,password):
        """
        transfer a file with SCP protocol
        """
        print "SCP:"+scp_cmd
        p = pexpect.spawn(scp_cmd)
        time.sleep(0.5)
        ssh_newkey = 'Are you sure you want to continue connecting'
        i = p.expect([ssh_newkey, '[pP]assword', "# ", pexpect.EOF,
                      pexpect.TIMEOUT], 120)
        if i == 0:  # add once in trust list
            p.sendline('yes')
            i = p.expect([ssh_newkey, '[pP]assword', pexpect.EOF], 2)

        if i == 1:
            time.sleep(0.5)
            p.sendline(password)
            p.expect("Exit status 0", 60)
        if i == 4:
            print "SCP TIMEOUT error %d" % i

        p.close()
    def close(self,force=False):
        if force is True:
            self.session.close()
        else:
            if self.isalive():
                self.session.logout()
                
                
if __name__ =="__main__":
    pdb.set_trace()
    ssh = SSHUtils("172.16.18.104","root","sxm20160225")
    ssh.send_expect("ls -l", "# ")
    print ssh.get_out_before()