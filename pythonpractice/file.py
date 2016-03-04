import os
root = 'D://share'
#result = os.listdir(root)

import string
def __get_all_files_in(folder, indent):
	folder = string.replace(folder, '\\', '/')
	print '    '*indent, folder.rpartition('/')[2]
	indent += 1
	files = os.listdir(folder)
	for f in files:
		if os.path.isfile(os.path.join(folder, f)):
			print '    '*indent, f#f.rpartition('.')[0]
		else:
			__get_all_files_in(os.path.join(folder, f), indent)

def get_all_files_in(folder):
	__get_all_files_in(folder, 0)
#get_all_files_in(root, 0)
get_all_files_in('//kwokph-3-w7/DBCR/LLPRPT/yyyymmdd')