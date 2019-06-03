# -*- coding:utf-8 -*-
#encoding=utf-8  #可以加中文注释

#from xml.dom import minidom

# 解析XML文件

import xlrd

#获取Root
def getRoot(path):
	path =  'E:\\test.xlsx'
	dom = xlrd.open_workbook(path)  	#打开xls文件
	print (type(dom)) 
	table = dom.sheets()[0]  			#打开第一张表
	return table

def getAllList(path):
	table = getRoot(path)
	nrows = table.nrows 				#获取表的行数
	ncols = table.ncols 				#获取表的行数
	# print (table.col_values(0))			#第一列的数据	
	# print (table.row_values(0))			#第一行的数据
	# col = table.col_values(0)
	row = table.row_values(0)	
	nameList = {}				
	for i in range(nrows):				
		if i == 0 :
			continue
		tabs = table.row_values(i)
		name = tabs[0]
		cnName = tabs[1]
		nameList[i-1] = {"name" : name,"cnName" : cnName}
	lens = len(nameList)
	#print nameList[0]["cnName"]
	for i in range(lens):
		print nameList[i]["name"] + nameList[i]["cnName"]
	return nameList	

#getAllList("asd")
