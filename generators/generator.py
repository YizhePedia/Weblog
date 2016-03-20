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
        self.html_dev_path = "../html/" # for html folder in dev
        self.titles_dev_path = "../html/titles/" # for titles folder in dev
        self.titles_server_path = "/titles/" # for titles folder on server
        self.pedia_dev_path = "../html/pedia/" # for pedia folder in dev
        self.pedia_server_path = "/pedia/" # for pedia folder on server
        
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

    def pediaHtmlImgFix(self,htmlFile):
        # load unfixed html
        pedia_html = codecs.open(self.pedia_dev_path+htmlFile,"r","utf-8")
        content = pedia_html.read()
        new_content = content.replace("img src=\"",
                            "img src=\""+self.pedia_server_path)
        # prevent over-replace
        new_content = new_content.replace(
                            self.pedia_server_path+self.pedia_server_path,
                            self.pedia_server_path)                      
        pedia_html.close()        
        # write fixed html
        pedia_html = codecs.open(self.pedia_dev_path+htmlFile,"w","utf-8")
        pedia_html.write(new_content)
        pedia_html.close()
        
    def generateHtml(self):
        # weblog enum
        wid,wv,wseries,wtopic,wkeyword,wurl=range(0,6)
        series_html = codecs.open(self.html_dev_path+"series.html","w","utf-8")
        series_count = -1
        last_series = ""
        title_html = codecs.open(self.html_dev_path + \
                        "titles-null.html","w","utf-8")
        for entry in self.wb_data:            
            if entry[wv]==0:
                break
            if entry[wseries] != last_series:
                title_html.close()
                series_count += 1
                last_series = entry[wseries]
                title_html = codecs.open(self.titles_dev_path + "titles-" \
                                + str(series_count) + ".html","w","utf-8")
                # wrtie series div
                series_html.write("<div class=\"series_entry\">\n\t" \
                    + "<span onmouseover=\"updateContent('#tframe','" \
                    + str(self.titles_server_path) + "titles-" \
                    + str(series_count) + ".html')\">\n\t" \
                    + str(entry[wseries]) + "\n\t</span>\n</div>\n")   
            # wrtie title div when aframe is iframe
#            title_html.write("<div class=\"title_entry\">\n\t" \
#                    + "<a class=\"tlink\" href=\"" + entry[wurl] \
#                    + "\" target=\"mpage\">\n\t" + str(entry[wtopic]) \
#                    + "\n\t</a>\n</div>\n")                       
            # write title div when aframe is div
            div_link = str(int(entry[0]))+"-"+entry[2]+"-"+entry[3]+".html" 
            self.pediaHtmlImgFix(div_link)
            title_html.write("<div class=\"title_entry\">\n\t" \
                    + "<span onclick=\"updateContent('#aframe','" \
                    + str(self.pedia_server_path) + div_link + "')\">\n\t" \
                    + str(entry[wtopic]) + "\n\t</span>\n</div>\n")                           
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
