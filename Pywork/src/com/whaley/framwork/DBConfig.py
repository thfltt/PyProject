# -*- coding: utf-8 -*-
'''
Created on 2017年3月24日

@author: hc
'''
import ConfigParser

configPath = "..\config\db.cfg"

class DBConfig():
    def __init__(self):
        self.charset="utf8"
        self.src = configPath
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(configPath)
    
    def getSections(self):
        return self.config.sections()
    def getOptionsInSection(self,section):
        return self.config.options(section)    
    def getOptionIntValue(self,section,option):
        return self.config.getint(section, option)
    def getOptionStrValue(self,section,option):
        return self.config.get(section, option)
    def getDBConfigTuple(self,section,host="host",username="username",password="password",database="database",charset="charset"):
        self.url =self.getOptionStrValue(section,".".join((section,host)))
        self.username=self.getOptionStrValue(section,".".join((section,username)))
        self.password= self.getOptionStrValue(section,".".join((section,password)))
        self.database = self.getOptionStrValue(section,".".join((section,database)))
        self.charset = self.getOptionStrValue(section,".".join((section,charset)))
        return (self.url,self.username,self.password,self.database,self.charset)
 
 
if __name__=="__main__":
    config = DBConfig()
    sections = config.getSections()
    for section in sections:
        print "section name is: %s" %section
        options = config.getOptionsInSection(section)
        print "option atrribute  is: %s" %options
        for option in options:
            print "option name is :%s" %option,", option value is:%s" %config.getOptionStrValue(section, option)
            
    print config.getDBConfigTuple("db1")
        