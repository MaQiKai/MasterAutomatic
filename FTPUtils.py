#coding=utf-8 
#通过FTP协议进行远程连接进行数据传输
import os
import shutil
import click
import paramiko
import utils
import sys 
reload(sys)
sys.setdefaultencoding('UTF-8')
def ftpDownload():
	worker_path = utils.getMainConfig("worker")
	ssh = paramiko.Transport(worker_path, 22)
	ssh.connect(username="playcrab", password="airmud")
	sftp = paramiko.SFTPClient.from_transport(ssh)
	config_path = utils.getMainConfig("worker_config_filePath")
	current_path = os.path.abspath(os.path.dirname(__file__))
	files = sftp.listdir(config_path)
	for f in files:
 		if "config" in f :
			src = os.path.join(config_path, f)
			des = os.path.join(current_path, f)
			sftp.get(src, des)
	ssh.close()	

def ftpUpload():
	worker_path = utils.getMainConfig("worker")
	ssh = paramiko.Transport(worker_path, 22)
	ssh.connect(username="playcrab", password="airmud")
	sftp = paramiko.SFTPClient.from_transport(ssh)
	ftp_config_path =  utils.getMainConfig("worker_config_filePath")
	ftp_config_name =  utils.getMainConfig("ftp_config_name")

	home_file_name = utils.getMainConfig("home_config_name")
	current_path = os.path.abspath(os.path.dirname(__file__))

	src = os.path.join(ftp_config_path, ftp_config_name)
	des = os.path.join(current_path, home_file_name)
	print ("workPath:" + src)
	print ("homePath:" + des)
	if os.path.exists(des):
		if sftp.listdir(ftp_config_path):
			print "打包机配置路径存在"
			sftp.put(des,src)
			print "上传升级序列配置文件成功！"
		else:
			print "打包机升级序列配置路径错误！"
	else:
		print "本地升级序列配置文件不存在！"
	ssh.close()	

def ftpCreateUpgrade():
	worker_path = utils.getMainConfig("worker")
	#实例化一个transport对象
	trans = paramiko.Transport(worker_path, 22)
	#建立连接
	trans.connect(username="playcrab", password="airmud")
	#将sshclient的对象的transport指定为以上的trans
	ssh = paramiko.SSHClient()
	ssh._transport = trans 
	filepath = os.path.join('/data/work/walle/master_walle',"upgrade_sequence.py")
	#结果放到stdout中，错误放在stderr中
	stdin,stdout,stderr = ssh.exec_command('python '+ filepath)
	print("stdin:" + stdout.read().decode()) 
	print "stderr:" + stderr.read().decode()

def ftpCreatePackage():
	worker_path = utils.getMainConfig("worker")
	#实例化一个transport对象
	trans = paramiko.Transport(worker_path, 22)
	#建立连接
	trans.connect(username="playcrab", password="airmud")
	#将sshclient的对象的transport指定为以上的trans
	ssh = paramiko.SSHClient()
	ssh._transport = trans 
	filepath = os.path.join('/data/work/walle/master_walle',"upgrade_sequence.py")
	#结果放到stdout中，错误放在stderr中
	stdin,stdout,stderr = ssh.exec_command('python '+ filepath)
	print("stdin:" + stdout.read().decode()) 
	print "stderr:" + stderr.read().decode()	