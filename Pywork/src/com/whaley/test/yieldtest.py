# -*- coding: utf-8 -*-
'''
Created on 2017年4月10日

@author: hc
'''
datas = [i+1  for i in range(10)]
def testyield(data):
    for i in data:
        yield i #any include yield statement in function return  generator

res1 = testyield(datas)
print res1 
print res1.next() 
print res1.next() 
