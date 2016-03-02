# encoding: UTF-8

def printFolder():
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

def findUniqueNumber():
    class Test(object):
        """get the unique value of a pair-exist number list"""
        def getValue(self, alist):
            result = 0
            #for i in alist:
            #    result = result^i
            result = eval('^'.join([str(i) for i in alist]))
            return result
    def test():
        alist = [1, 1, 32, 32, 5, 6, 7, 8, 9, 8, 7, 6, 5, 1009, 1009, 200001, 200001]
        aTest = Test()
        print 'test...'
        assert aTest.getValue(alist) == 9, 'Wrong answer'
        print 'successful!'
    return test

def testCopy():
    #d = {'a':'1', 'b':'2'}

    #print d.get('c', 'b')
    #print d.setdefault('c', '3')
    #print d.get('c')
    def copy():
        x = {"name":"qiwsir", "lang":["Python", "java", "c"]}
        y = x.copy()
        y["lang"].remove("c")
        print y
        print x
    return copy

findUniqueNumber()()
#testCopy()()
