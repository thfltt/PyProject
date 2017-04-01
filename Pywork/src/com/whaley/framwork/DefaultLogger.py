# -*- coding: utf-8 -*-
'''
Created on 2017年3月29日

@author: hc
'''
import logging
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname) ',datefmt="%Y-%m-%d %H:%M:%S")
class DefaultLogger():
    def __init__(self,level=logging.DEBUG,msgfmt='%(asctime)s %(levelname)s %(filename)s:%(funcName)s %(thread)d %(threadName)s [line:%(lineno)d] %(message)s',datefmt="%Y-%m-%d %H:%M:%S"):
        self.level = level
        self.msgfmt = msgfmt
        self.datefmt = datefmt
        #logging._acquireLock()
        logging.basicConfig(level=self.level,format=self.msgfmt,datefmt=self.datefmt)
        #logging._releaseLock()
        
    def getLogger(self,name):
        logger = logging.getLogger(name)
#        console = logging.StreamHandler()
#        formatter = logging.Formatter(self.msgfmt)
#        console.setFormatter(formatter)
#        logger.addHandler(console)
#        logger.setLevel(logging.DEBUG)
        return logger


if __name__ == "__main__":
    logger = DefaultLogger().getLogger("TEST")
   
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    