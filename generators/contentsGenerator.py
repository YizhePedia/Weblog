# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 07:00:23 2016

@author: Rick Liu
@usage: generate contents for wechat public account and blog from contents.csv
"""

import xlrd

# Generator class
class contentsGenerator:
    def contentsGenerator(self):
        self.data = {}
        self.nrows = 0
        self.ncols = 0
        
    def loadXLSX(self):
        try:
            bk = xlrd.open_workbook("contents.xlsx")            
        except:
            print("contents.xlsx can not be loaded")
        try:
            sh = bk.sheet_by_name("Weblog")            
        except:
            print("Weblog sheet cannot be loaded")            
        self.nrows = sh.nrows
        self.ncols = sh.ncols
        

# Auto-runner for testing
if __name__=='__main__':
    cg = contentsGenerator()
    cg.loadXLSX()
    print(cg.ncols)
    print(cg.ncols)
