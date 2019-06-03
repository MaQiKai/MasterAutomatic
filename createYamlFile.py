#!/usr/bin/python
#coding=utf-8

import yaml
import os
import json
import shutil
import sys
import utils
from os import path
reload(sys)
sys.setdefaultencoding('utf8')


 
def addDefaultContent(datas):
	kongge = "    "
	datas.append("default: ")
	datas.append(kongge + "parameter: ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'os_platform' ")
	datas.append(kongge + kongge + kongge + "value: 'ios' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'is_pngquant'")
	datas.append(kongge + kongge + kongge +"value: 'true' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'image_format' ")
	datas.append(kongge + kongge + kongge +"value: 'pvr' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'is_encrypt' ")
	datas.append(kongge + kongge + kongge +"value: 'true' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'open_etc' ")
	datas.append(kongge + kongge + kongge +"value: '1' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'lua_compile' ")
	datas.append(kongge + kongge + kongge +"value: 'true' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'update_subpackage_size' ")
	datas.append(kongge + kongge + kongge +"value: '100' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'lua_compile_zip' ")
	datas.append(kongge + kongge + kongge +"value: 'true' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'assets_pack' ")
	datas.append(kongge + kongge + kongge +"value: 'true' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + kongge + "name: 'mini_package_test' ")
	datas.append(kongge + kongge + kongge +"value: 'false' ")
	datas.append(kongge + kongge + "- ")
	datas.append(kongge + kongge + "- ")


def createFile(configs):
	kongge = "    "
	current_path = os.path.abspath(os.path.dirname(__file__))
	print(current_path)
	fileName = utils.getMainConfig("upgrade_config_name")
	file_path = os.path.join(current_path,fileName)
	fr = open(file_path,'wb+')
	#yaml.load(fr) 
	datas =[]
	addDefaultContent(datas)
	datas.append("upgrade_sequence: ")
	for index in range(len(configs)):
		name = configs[index]["name"]
		cnName = configs[index]["cnName"]
		upperName = name.upper()
		datas.append(kongge + "- ")
		datas.append(kongge + kongge + "upgrade_path:  ")
		datas.append(kongge + kongge + kongge + "name: " + "'" + "IOS_MINI_" + upperName + "'")
		datas.append(kongge + kongge + kongge + "description: " + "'" + "ios马甲包-" + cnName + "'")
		datas.append(kongge + kongge + "parameter: 	" + " ")
		datas.append(kongge + kongge + kongge + "- ")
		datas.append(kongge + kongge + kongge + kongge + "name: " + "'mini_package_channel'")
		datas.append(kongge + kongge + kongge + kongge + "value: " + "'" + name + "'")
		datas.append(kongge)

	for i in datas:
		fr.write(i + '\n')
	fr.flush()
	fr.close() 
	#将python对象写入文档
	# yaml.dump(datas,fr) 
	fr.close()
