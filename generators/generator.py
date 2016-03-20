# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 07:00:23 2016

@author: Rick Liu
@usage: generate contents for wechat public account and blog from contents.csv
"""


import xlrd
import codecs

# Generator class
class generator:
    def __init__(self):
        self.wb_nrows = 0
        self.wb_ncols = 0
        self.wb_data = []
        self.html_path = "../html/"

        
    def loadXLSX(self):
        try:
            bk = xlrd.open_workbook("config.xlsx")            
        except:
            print("contents.xlsx can not be loaded")
        # load Weblog sheet
        try:
            sh = bk.sheet_by_name("Weblog")            
            self.wb_nrows = sh.nrows
            self.wb_ncols = sh.ncols
            self.loadWeblog(sh)
        except:
            print("Weblog sheet cannot be loaded")           

        
    def loadWeblog(self,sh):        
        for ri in range(1,self.wb_nrows):
            row_data = []
            for ci in range(0,self.wb_ncols):
                row_data.append(sh.cell(ri,ci).value)                    
            self.wb_data.append(row_data)
    
    def generateHtml(self):
        # weblog enum
        wid,wv,wseries,wtopic,wkeyword,wurl=range(0,6)
        series_html = codecs.open(self.html_path+"series.html","w","utf-8")
        series_count = -1
        last_series = ""
        title_html = codecs.open(self.html_path+"titles-null.html","w","utf-8")
        for entry in self.wb_data:
            if entry[wv]==0:
                break
            if entry[wseries] != last_series:
                title_html.close()
                series_count += 1
                last_series = entry[wseries]
                title_html = codecs.open(self.html_path + "titles-" \
                                + str(series_count) + ".html","w","utf-8")
                # wrtie series div
                series_html.write("<div class=\"series_entry\">\n\t" \
                    + "<span onmouseover=\"updateContent('#tframe','titles-" \
                    + str(series_count) + ".html')\">\n\t" \
                    + str(entry[wseries]) + "\n\t</span>\n</div>\n")   
            # wrtie title div
            title_html.write("<div class=\"title_entry\">\n\t" \
                    + "<a class=\"tlink\" href=\"" + entry[wurl] \
                    + "\" target=\"mpage\">\n\t" + str(entry[wtopic]) \
                    + "\n\t</a>\n</div>\n")                                                         
        series_html.close()    
        title_html.close()

    def runner(self):
        cg = generator()
        cg.loadXLSX()
        cg.generateHtml()

# Auto-runner for testing
if __name__=='__main__':
    cg = generator()
    cg.loadXLSX()
    cg.generateHtml()
