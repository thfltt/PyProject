# -*- coding: utf-8 -*-
'''
Created on 2017年3月24日

@author: hc
'''
import MySQLdb
import datetime
from DBConfig import DBConfig
from DefaultLogger import DefaultLogger
class DBUtils():
    def __init__(self,dbConfig):
        self.host,self.user,self.passwd,self.db,self.charset =dbConfig
        self.conn= MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.logger = DefaultLogger().getLogger("DBUtils")

   
   
    def CRD_record(self,sql,operation):
        print "sql:"+sql
        cursor= self.conn.cursor()
        res= cursor.execute(sql)
        if(res !=0):
            print"%s Success" %(operation)
        else:
            print "%s Failed" %(operation)
        self.conn.commit()
        self.close()
        
   
    def qeuey_record(self,sql):
        cursor= self.conn.cursor()
        res= cursor.execute(sql)
        
        if(res!=0):
            datas = cursor.fetchall()
            #self.logger.info("datas type:%s" %type(datas))
            print "datas type:%s" %type(datas)
            for row in datas:
                for col in row:
                    print col,
                print"\n"
        else:
            print "no data found!"   
         
        
   
    def add_batch_datas(self,sql,datas):
        cursor= self.conn.cursor()
        res = cursor.executemany(sql,datas)
        self.conn.commit()
        self.close()
        return res
        
   
   
    def query_record_dict(self,sql):
        cursor = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        res = cursor.execute(sql)
        if(res !=0):
            datas = cursor.fetchall()
            #self.logger.info("datas type:%s" %type(datas))
            #print "datas type:%s" %type(datas)
            for row in datas:#row type is dict
                pass
                #self.logger.info(row)
#                print "\n"
#                print "position_code:%s" %row['position_code'],
#                print "position_name:%s" %row['position_name'],
#                print "position_name_en:%s" %row['position_name_en'],
#                print "status:%d" %row['status'],
#                print "create_user:%s" %row['create_user'],
#                print "create_date:%s" %row['create_date'],    
#                print "\n"
    
        else:
            print "no data found!"
        return datas
       
    def heart_beat_test(self):
        return self.qeuey_record("select version()")
        
    def close(self):
        self.conn.close()
      
     


if __name__=="__main__":
    config = DBConfig()
    dbParams=config.getDBConfigTuple("db1")
    dbUtils = DBUtils(dbParams)
    dbUtils.heart_beat_test()
    print datetime.datetime.now()
    #dbUtils.qeuey_record("select * from position")
    dbUtils.query_record_dict("select * from position")
    dbUtils.close()
    #dbUtils.CRD_record("insert into position (`position_code`,`position_name`, `status`,`create_user`,`create_date`) values ( '%s','%s',%d,'%s','%s')"%("123","test",1,"syspython",datetime.now()), "insert")
    #dbUtils.CRD_record("update position set position_name='测试工程师' where position_code='1200158'", "update")
    #dbUtils.CRD_record("delete from  position where position_code='1200161'" , "delete")
    
