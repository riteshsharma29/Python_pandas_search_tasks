#!/usr/bin/python
# coding: utf-8 -*-

import pandascls
import pandas as pd
import xlrd,sys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

filename = sys.argv[1]
searchstr = sys.argv[2]

#create a instance or object of class Datasci 

df = pandascls.Datasci()

wb = xlrd.open_workbook(filename)
p = wb.sheet_names()

text_file = open("Output.txt", "w")

for sheetname in p:

	dataf = df.readexcel(filename,sheetname,df)

	mylist = dataf.values.T.tolist()

	for lst in mylist:
		for x in range(len(lst)):
			fndstr = lst[x]
                        fndstr = str(fndstr)
			if str(searchstr) in fndstr:
				print lst[x],sheetname
				text_file.write(str(lst[x]) + ", sheetName: " + sheetname + "\n")
