# -*- coding: utf-8 -*-
'''
Created on 2017年3月23日

@author: hc
'''

import xlrd

import traceback
class Execl():
    
    def get_file_handler(self,filename):
        try:
            return xlrd.open_workbook(filename)
        except Exception ,e:
            print e 
            traceback.print_exc()
            




if __name__=="__main__":
    execlHandler = Execl()
    data = execlHandler.get_file_handler("D:\workspace\Pywork\src\whaleypost.xls")
    sheet = data.sheets()[0]
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        for j in range(cols):
            print sheet.cell_value(i,j)