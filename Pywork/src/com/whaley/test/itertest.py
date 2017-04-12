# -*- coding: utf-8 -*-
'''
Created on 2017年4月10日

@author: hc
'''
data =( i for i in range(6) )
data1 = {str(i):i for i in range(6)}
print type(data)

while True:
    try:
        print data.next()
    except StopIteration,e:
        print e 
        print "all over"
        break
print type(data1) ,data1