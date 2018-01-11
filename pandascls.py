#!/usr/bin/python

import pandas as pd
import json

class Datasci:

	def readexcel(self,filename,sheetnm,df):
		self.filename = filename
		self.sheetnm = sheetnm
		self.df = pd.read_excel(self.filename,sheetname=self.sheetnm)
		return self.df

	def readcsv(self,filename,df):
		self.filename = filename
		self.df = pd.read_csv(self.filename)
		return self.df

	def readhtml(self,url,df):
		self.url = url
		self.df = pd.read_html(self.url)
		return self.df


