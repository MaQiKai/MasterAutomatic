import os
import click
import time
import config


# @click.command()
# @click.option('-d/-nd', '--debug', default=False, help=u'debug')
# @click.option('-res', '--res', default='debug', help=u'asset res:debug release online')
# @click.option('-type', '--type', default=2, help=u'svn :1:commit,2:update')


def run(**options):
	begin(options)

def begin(options):
	assets_path = config.setting['asset_path_' + options['res']]
	assets_revision = do_svn_op(assets_path,options['type'])
	print('asset revision is ' + assets_revision)

	config_path = config.setting['config_path']
	config_revision = do_svn_op(config_path,options['type'])
	print('config revision is ' + config_revision)

def do_svn_op(path,typeIndex):
	gotoTargetPath(path)
	if typeIndex == 1:
		doSvnCommit()
	elif typeIndex == 2:
		doSvnUpdate()
	else:
		print('typeIndex only includs 1 and 2')

	revision = getSvnCommitVersion()
	return revision

def gotoTargetPath(path):
	pathshell = path
	print(pathshell)
	os.chdir(pathshell)

def doSvnCommit():
	svn_commit = 'svn commit -m \'svn commit\''
	print(svn_commit);
	os.system(svn_commit)

def doSvnUpdate():
	svn_update = 'svn update'
	os.system(svn_update)


def getSvnCommitVersion():
	svn_info = 'svn info';
	p = os.popen(svn_info);
	x = p.readlines();
	svnRevision = 0;
	for line in x:X
		if line.find('Revision') >= 0:
			svnRevision = int(line.strip().split(':')[-1])
	
	return svnRevision





if __name__ == '__main__':
    run()