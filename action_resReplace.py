#coding=utf-8

#Filename:    
#Author:      wangshuai 
#Datetime:    2018-04-16
#Description: File description
#

import shutil
import subprocess
import os
import sys
from Tkinter import *
import tkFileDialog
from PIL import Image 
import hashlib
import utils  
import XMLFilePars
import createYamlFile
import FTPUtils



resFlag = False
XMLFlag = False




if __name__ == '__main__':
    #runRes("E:/data/work/a","E:/data/work/b")
    root = Tk()
    root.title("自动打包工具")

    root.geometry('550x300')                 #是x 不是*
    
    frm = Frame(root)
    Label(frm, text="让我们愉快的自动打包吧" ,cursor = "cross",font=('Arial', 15)).pack(side=TOP)
#资源输入路径
    frm_L = Frame(frm)
    intputLabel = Label(frm_L, text='请选择资源输入路径', font=('Arial', 15))
    intputLabel.pack(side=RIGHT)
    def inputputClick(): 
        filename = tkFileDialog.askopenfilename(initialdir = 'E:')
        print ("InputFilePath:",filename)
        intputLabel.config(text=filename)
    Button(frm_L, text='输入路径',bg = "red", font=('Arial', 15),command=inputputClick).pack(side=LEFT)
    frm_L.pack(side=TOP)

#资源输出路径
    frm_R = Frame(frm)
    def outputputClick():
        filename = tkFileDialog.askdirectory(title = "选择文件夹")
        print ("OnputFilebPath",filename)
        outputLabel.config(text=filename)
    Button(frm_R, text='输出路径',bg = "red", font=('Arial', 15),command=outputputClick).pack(side=LEFT)
    outputLabel =Label(frm_R, text='请选择资源输出路径', font=('Arial', 15))
    outputLabel.pack(side=RIGHT)
    frm_R.pack(side=TOP)

#选择XML文件
    frm_3 = Frame(frm )
    def xmlPathClick():
        filename = tkFileDialog.askopenfilename(title = "选择文件")
        print ("XMLFilebPath",filename)
        xmlPathLabel.config(text=filename)

    Button(frm_3, text='XML文件路径', bg = 'red',font=('Arial', 15),command=xmlPathClick).pack(side=LEFT)
    xmlPathLabel =Label(frm_3, text='请选择XML路径', font=('Arial', 14))
    xmlPathLabel.pack(side=RIGHT)
    frm_3.pack(side=TOP)


    frm.pack()

  

    def imputResource():
        
        flag = utils.unzip(intputLabel['text'],outputLabel['text'])
        # print (intputLabel['text'] + ':' + outputLabel['text'] + ':' +xmlPathLabel['text'] )
        if flag:
            print ("导入资源成功")
            global resFlag
            resFlag = True


    def xmlFilePars():
        global resFlag
        # if not resFlag:
        #     print ("请先导入资源")
        #     return 
        flag = utils.checkXMLFile(xmlPathLabel['text'])
        if flag :
            data = XMLFilePars.getAllList(xmlPathLabel['text'])
            
            createYamlFile.createFile(data)
            global XMLFlag
            XMLFlag = True

    def createUpgrade():
        global XMLFlag
        if XMLFlag :
            ftpUtils.ftpUpload()


    def Click():
        # flag = utils.checkXMLFile(xmlPathLabel['text'])
        # print flag  
        # if not flag :
        exit()
        # root.quit() 
        # os.system('pause')  
 
    Button(root, text='导入资源', font=('Arial', 15),command=imputResource).pack(side=TOP)
    Button(root, text='通过XML文件生成升级序列配置文件', font=('Arial', 15),command=xmlFilePars).pack(side=TOP)
    Button(root, text='连接打包机生成升级序列', font=('Arial', 15),command=createUpgrade).pack(side=BOTTOM)
    Button(root, text='开始批量打包流程', font=('Arial', 15),command=createUpgrade).pack(side=BOTTOM)
    Button(root, text='确定', font=('Arial', 15),command=Click).pack(side=BOTTOM)
 
    root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True
    root.mainloop()
 