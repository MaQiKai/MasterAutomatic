import os
import click
import datetime  
import time
import utils
import subprocess

@click.command()
@click.option('-d/-nd', '--debug', default=False, help=u'debug')
@click.option('-cb', '--cbranch', default=True, help=u'C Bramch')
@click.option('-lb', '--luabranch', default=True, help=u'Lua Bramch')

def run(**options):
	make_tag(options)

def getTagName(branchName,path):
	gotoTargetPath(path)
	changeBranch(branchName)

	today = datetime.date.today()
	prefix = str(today.year % 100)
	if today.month < 10:
		prefix = prefix + '0'
	prefix = prefix + str(today.month)
	if today.day < 10:
		prefix = prefix + '0'
	prefix = prefix + str(today.day)
	
	p = os.popen('git tag') 
	x = p.readlines()
	maxIndex = 0
	for line in x:
		if line.find(prefix) >= 0:
			index  = int(line.strip().split(".")[-1]) % 100
			if index > maxIndex:
				maxIndex = index
	tagIndex = maxIndex
	if maxIndex < 10: 
		tagIndex = "0" + str(maxIndex + 1)
	else:
		tagIndex = str(maxIndex + 1)
	newtag  = prefix +'.'+ tagIndex
	return branchName + '.' + newtag

def pushNewTag(newtag):
	tagshell = 'git tag -a ' + newtag + ' -mx'
	os.system(tagshell) 
	os.system("git push origin " + newtag ) 
def createBranch(branchName):
	tagshell = 'git checkout ' + '-b' + branchName;
	os.system(tagshell)


def changeBranch(branchName):
	tagshell = 'git checkout ' + branchName; 
	print(tagshell)
	os.system(tagshell)
	
def gotoTargetPath(path):
	pathshell = path
	print(pathshell)
	os.chdir(pathshell)
	#retval = os.getcwd()
	#print(retval)

def make_tag(options):
	cpath = config.setting['c_path']
	print(cpath)
	ctag = getTagName(options['cbranch'],cpath)
	pushNewTag(ctag)

	luapath = config.setting['lua_path']
	print(luapath)
	luatag = getTagName(options['luabranch'],luapath)
	pushNewTag(luatag)


# if __name__ == '__main__':
#     run()

def teseMakeTag():
	cpath = utils.getMainConfig("c_path")
	print(cpath)
	os.chdir(cpath)
	str = "git checkout online"
	current_path = os.getcwd()
	print(current_path)
	# idx = os.popen(str)
	idx = os.popen(str)
	print idx


teseMakeTag()
