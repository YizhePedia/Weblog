# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:39:46 2016

@author: Rick Liu
@usage: Use to reformat the csv exported from mindmap
@memo: In my mindmanager & excel, utf-8-dom or uft-8-sig is default encoding
"""

import codecs
import csv

class mmapCsvReformat():
    def __init__(self):
        self.data = []
        
    def readCsv(self,source):
        try:
            # mmap->csv using utf-8-bom encoding
            sf = codecs.open(source,"r","utf-8-sig")
            reader = csv.reader(sf)
        except:
            print("Source file ("+source+") cannot be loaded")
        try:
            for line in reader:                
                line_data = []
                for data in line:
                    if data!="":
                        line_data.append(data)
                self.data.append(line_data)
            # Drop first line
            del self.data[0]
        except:
            print("Data in csv cannot be loaded")
        finally:
            sf.close()

    def mergeListToString(self,lst):
        s = lst[0] + " : "
        for entry in lst[1:]:
            s += (str(entry)+"   ")
        return(s)
    
    def dataReform(self):
        new_data = []
        last_topic = ""
        for row in self.data:
            series = row[0]
            topic = row[1]
            keyword = ""
            if len(row)>2:
                keyword = self.mergeListToString(row[2:])                            
            if topic!=last_topic:
                new_data.append([series,topic,keyword])
                last_topic = topic
            else:
                # append string to last row            
                new_data[-1][-1] += ("\n" + keyword)            
        self.data = new_data
    
    def csvOutput(self,fname):
        try:
            f = codecs.open(fname,"w","utf-8-sig")
            writer = csv.writer(f)
        except:
            print("Output file cannot be opened")
        try:
            for row in self.data:
                writer.writerow(row)
        except:
            print("Cannot write data into new csv")
        finally:
            f.close()
    
    def runner(self,icsv,ocsv):
        mcr = mmapCsvReformat()
        mcr.readCsv(icsv)
        mcr.dataReform()
        mcr.csvOutput(ocsv)
        
# Auto runner for testing
if __name__=="__main__":
    mcr = mmapCsvReformat()
    mcr.readCsv('test.csv')
    mcr.dataReform()
    mcr.csvOutput('output.csv')