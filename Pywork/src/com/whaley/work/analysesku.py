# -*- coding: utf-8 -*-
'''
Created on 2017年4月7日

@author: hc
'''
from com.whaley.framwork.DBUtils import DBUtils
from com.whaley.framwork.DBConfig import DBConfig




config = DBConfig()
dbParams=config.getDBConfigTuple("db2")
dbUtils = DBUtils(dbParams)
dbUtils.heart_beat_test()

def get_sku_info(params):
    sku_id = ''
    sale_price=''
    param_array = params.split("&")
    for param in param_array:
        if param.find(u'sku_id') !=-1:
            sku_id = param.split("=")[1]
        if param.find(u'sale_price')!=-1:
            sale_price = param.split("=")[1]
            
      
    return (sku_id,sale_price)
    
res_lst = dbUtils.query_record_dict("SELECT * FROM user_operation_log WHERE domain LIKE '%product%' AND moudle LIKE '%sku%' AND (util LIKE '%updatesku%' OR util LIKE '%addsku%')")
records =[]
for res in res_lst :
    param_text = res['param_text']
    create_date = res['create_date']
    sku_id,sale_price = get_sku_info(param_text)  
    record = []
    record.append(sku_id)
    record.append(sale_price)
    record.append(create_date)
    records.append(tuple(record))
    #print (sku_id,sale_price,create_date)
print tuple(records)
sql = "insert into sku_price_history(sku_id,sale_price,create_date) values(%s,%s,%s)"    
rows = dbUtils.add_batch_datas(sql, records)    
print "%d added!" %rows

