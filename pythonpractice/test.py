
import os

path = "."

def listBasename(folder):
	for fname in os.listdir(folder):
		#print(fname[:fname.rindex('.')])
		#print((lambda f: f[:f.rindex('.')])(fname))
		print fname
	print('-' * 20)

#listBasename('.')
def localAreaFileList(folder):
	print folder
	#os.system(r"net use n: //10.222.1.149/share")
	listBasename(folder)
localAreaFileList('//kwokph-3-w7/DBCR/LLPRPT')
