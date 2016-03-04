# encoding: UTF-8

import os
import subprocess
import sys

def testOS():
	os.system('ping www.baidu.com')

def testCmdFromFile():
	f = open('cmd.txt', 'r')
	cmd = f.readline()
	os.system(cmd)
	f.close()

def testSubprocess():
	# reload(sys)
	# sys.setdefaultencoding('utf-8')

	# os.system('set PYTHONIOENCODING=utf8')
	print(sys.getdefaultencoding())
	ioencoding = sys.stdout.encoding
	print(sys.stdout.encoding)
	try:
		p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# while 1:
		# 	buff = p.stdout.readline()
		# 	print(buff)
		# 	if buff == '' and p.poll() != None:
		# 		break
		# print(p.stdout.read())
		# print(p.communicate())
		infos = p.stdout.readlines()
		# print(infos)
		for i in infos:
			print(i.decode(ioencoding))
		# unicode_text = u''.join(infos)
		# print(unicode_text)
		p.wait()
	except Exception as _ex:
		print('ERROR: %s' % str(_ex))

# testOS()
# testCmdFromFile()
testSubprocess()