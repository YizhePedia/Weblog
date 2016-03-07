# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 07:00:23 2016

@author: Rick Liu
@usage: generate the contents for wechat public account and blog from contents.csv
"""

import csv

# Generator class
class contentsGenerator:
    def contentsGenerator(self):
        self.data = {}
        
    def loadCSV(self):
        csvfile = file('contents.csv','r')
        reader = csv.reader(csvfile)
        for line in reader:
            print(line)
        csvfile.close()
        

# Auto-runner for testing
if __name__=='__init__':
    print("Yes")    
