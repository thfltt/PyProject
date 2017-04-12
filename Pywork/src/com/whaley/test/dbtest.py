'''
Created on Apr 12, 2017

@author: root
'''
from com.whaley.framwork.DBUtils import DBUtils
from com.whaley.framwork.DBConfig import DBConfig

config = DBConfig()
dbParams=config.getDBConfigTuple("db2")
dbUtils = DBUtils(dbParams)
dbUtils.heart_beat_test()