#!/usr/bin/python
#coding=utf-8

import yaml
import os
import json
import zipfile
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

main_config = None

def getMainConfig(key = None):
    global main_config
    if main_config == None:
        self_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(self_dir, 'config.yaml')
        print config_path
        if not os.path.exists(config_path):
            print("config.yaml 文件不存在，请添加")
            exit()
        stream = file(config_path, 'r')
        main_config = yaml.load(stream)
    if key != None:
        if main_config.has_key(key):
            return main_config[key]
        else:
            return None
    return main_config

def getTempPath():
    self_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    temp_path = os.path.join(self_dir, 'temp')
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)
    return temp_path

def unzip(zipName,desDir):
    r = zipfile.is_zipfile(zipName)
    if r:
        print  zipName + "isZip"
        fz = zipfile.ZipFile(zipName,'r')
        for file in fz.namelist():
            fz.extract(file,desDir)

        tempPath = os.path.join(desDir, "__MACOSX")
        print("__MACOSX   Path:"  + tempPath)
        if os.path.isabs(tempPath):
            print("有__MACOSX")
            if os.path.isdir(tempPath):
                print("__MACOSX是一个路径")
                shutil.rmtree(tempPath) 
                print("删除__MACOSX")
        else:
            print("__MACOSX不存在")
        return True
    else:
        print "导入文件错误，请导入zip文件"        
        return False

def zip(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
    
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()

def checkXMLFile(path):
    flag =  path.find('xlsx')
    if flag == -1 :
        print("XML文件格式不对，请重新选择后缀名为.xlsx的文件")
    return  (not flag == -1 and True) or False  
                
            

if __name__ == '__main__':
    # getMainConfig('')
    pass