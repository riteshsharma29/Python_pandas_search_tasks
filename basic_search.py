#!/usr/bin/python
# coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('findmatch.xls',sheetname='child')

#Method I

# To find a string in Dataframe column
#x = df.loc[df['Column Name'] == 'Search String']

#####################################################################################################################

#Method II

#Converts a Dataframe into a nested list # column 1 values will be stored in list[0], column 2 values will be stored in list[1] and So On and So Forth
mylist = df.values.T.tolist()

# If the string is found Boolean value will be returned
x = 'Search string' in [j for i in mylist for j in i]

#finding string & substring
for x in range(len(mylist)):
     for y in range(len(mylist[x])):
         if 'Wilson' in mylist[x][y]:
             print mylist[x][y]
