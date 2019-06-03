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



def createFile(configs):
	kongge = '\t'
	current_path = os.path.abspath(os.path.dirname(__file__))
	print(current_path)
	fileName = utils.getMainConfig("createPackageConfig")
	file_path = os.path.join(current_path,fileName)
	print file_path
	fr = open(file_path,'wb+')
	datas =[]

	count = 1 
	for index in range(len(configs)):
		paramList = {
			"upgrade_path" : "IOS_MINI_JHDMX", 
			"region" : "china", 
			"platform" : "ourpalm", 
			"deployment" : "online", 
			"asset" : "75629", 
			"config" : "75629", 
			"script" : "online.mini.190219.01", 
			"frontend" : "online.mini.shj.181114.01", 
			"backend" : "19.2.1.190219.01", 
			"vms" : "encrypt.20171021.01", 
			"pctools" : "1",
			"kakura" : "master2processtime.20180409.01",
			"abaddon" : "master.170317.01",
			"configbanshu" : "75629",
			"global" : "online.190118.02",
			"battle_config" : "75629",
			"mtool" : "75629",
		}
		datas.append(count + ": ")
		datas.append(kongge + "upgrade_path:  " + paramList["upgrade_path"] )
		datas.append(kongge + "region:  " + paramList["region"])
		datas.append(kongge + "platform:  " + paramList["platform"])
		datas.append(kongge + "deployment:  " + paramList["deployment"])
		datas.append(kongge + "tag:  ")
		datas.append(kongge + kongge + "asset: " + paramList["asset"])
		datas.append(kongge + kongge + "config: " + paramList["config"])
		datas.append(kongge + kongge + "script: " + paramList["script"])
		datas.append(kongge + kongge + "frontend: " + paramList["frontend"])
		datas.append(kongge + kongge + "backend: " + paramList["backend"])
		datas.append(kongge + kongge + "vms: " + paramList["vms"])
		datas.append(kongge + kongge + "pctools: " + paramList["pctools"])
		datas.append(kongge + kongge + "kakura: " + paramList["kakura"])
		datas.append(kongge + kongge + "abaddon: " + paramList["abaddon"])
		datas.append(kongge + kongge + "configbanshu: " + paramList["configbanshu"])
		datas.append(kongge + kongge + "global: " + paramList["global"])
		datas.append(kongge + kongge + "battle_config: " + paramList["battle_config"])
		datas.append(kongge)
		count = count + 1

	yaml.load(fr) 
	for i in datas:
		fr.write(i + '\n')
	fr.flush()
	fr.close() 

createFile()