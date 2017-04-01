# -*- coding: utf-8 -*-
'''
Created on 2017年3月28日

@author: hc
'''
import time
from datetime import datetime,timedelta

print "time.time():%f" %time.time()
print "time.clock():%f" %time.clock()
#time.sleep(5)

print "time.gmtime():%s"%time.gmtime()
print "time.localtime():%s"%time.localtime()
print "time.mktime(time.gmtime()):%s"%time.mktime(time.gmtime())

print "datetime.now():%s"%datetime.now()

t1 = datetime(2016,7,4,19,30,59)
t2 = datetime(2016,8,4,19,30,59)
delta1 = timedelta(seconds = 600)
delta2 = timedelta(weeks = 3)

print "t1 + delta1: %s" %(t1 + delta1)
print "t1 + delta2:%s" %(t1 + delta2)
print " t2-t1:%s" %(t2-t1)

print "delta1:%s" %delta1
print "delta2:%s" %delta2

print "t1 :%s" %t1
print "t2 > t1:%s " %(t2 > t1)

fmt = "output-%Y-%m-%d-%H%M%S.txt" 
str1    = "output-1997-12-23-030000.txt" 
t      = datetime.strptime(str1, fmt)
print t

print t1.weekday()
