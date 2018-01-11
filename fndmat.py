#!/usr/bin/python
# coding: utf-8 -*-

import pandas as pd
import xlwt,re

df1 = pd.read_excel("findmatch.xls",sheetname="parent")
df2 = pd.read_excel("findmatch.xls",sheetname="child")

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("results",cell_overwrite_ok=True)

count = 0
for x,y in df1.values:
        x = x.encode('utf-8')
	vals_1 = str(x).replace("NZS_","").replace(" ","").replace("&","and")
        vals_1 = vals_1.lower()
	vals_2 = str(y)
        sheet1.write(count, 0, x)
        sheet1.write(count, 1, y)
        for a,b in df2.values:
            a = a.encode('utf-8')
            vals_3 = str(a).replace(" ","").replace("&","and")
            vals_3 = vals_3.lower()
            vals_3 = vals_3.split(":")
            if str(vals_3[0]) == vals_1 and vals_2 == str(b):
                print "" #str(vals_3[0]),vals_1,vals_2,str(b)
                sheet1.write(count, 4, "FOUND")
            f = re.search(vals_1,str(vals_3[0]))
            if f and vals_2 == str(b):
                print "" #str(vals_3[0]),vals_1,vals_2,str(b)
                sheet1.write(count, 4, "FOUND")
            s = re.search(str(vals_3[0]),vals_1)
            if f and vals_2 == str(b):
                print "" #str(vals_3[0]),vals_1,vals_2,str(b)
                sheet1.write(count, 4, "FOUND")
        count += 1


book.save("output.xls")



