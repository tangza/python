# encoding: UTF-8

__author__ = 'Zack Tang'

import os

path = "D:\GitRoot\OLLReport\DBScript\ollrsprd-hllp_scisp_admin\packages"

for dfile in os.listdir(path):
	# j = dfile.rindex('.')
	# basename = dfile[:j]
	# print('basename: ', basename)
	# newpath = os.path.join(path, basename + '.sql')
	newpath = os.path.join(path, 'Z_' + dfile)
	oldpath = os.path.join(path, dfile)
	print('newpath: ', newpath)
	print('oldpath: ', oldpath)
	os.rename(oldpath, newpath)