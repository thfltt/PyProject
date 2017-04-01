# -*- coding: utf-8 -*-
'''
Created on 2017年3月25日

@author: hc
'''
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