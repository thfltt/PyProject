# -*- coding: utf-8 -*-
'''
Created on 2017年4月10日

@author: hc
'''
import uuid
print uuid.uuid1()
print uuid.uuid4()
print uuid.uuid5(uuid.NAMESPACE_DNS, "whaley.cn")