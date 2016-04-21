#! python2
# -*- coding: utf8 -*-
import os, urllib2, re, urllib

#path = "."

#def listBasename(folder):
#	for fname in os.listdir(folder):
#		#print(fname[:fname.rindex('.')])
#		#print((lambda f: f[:f.rindex('.')])(fname))
#		print fname
#	print('-' * 20)

##listBasename('.')
#def localAreaFileList(folder):
#	print folder
#	#os.system(r"net use n: //10.222.1.149/share")
#	listBasename(folder)
#localAreaFileList('//kwokph-3-w7/DBCR/LLPRPT')

#print help(zip)
#print [x^y for x, y in zip(a, b)]

def test():
    con=urllib2.urlopen('http://quote.eastmoney.com/hk/00700.html?from=BaiduAladdin')
    data = con.read().decode('utf-8')
    #print con.headers.getheader('Content-Type')
    li = re.findall('<div.*?<div.*?<li><div.*?<a .*?>(.*?)</a>', data, re.S)
    print li
    l = [s.encode('gbk') for s in li]
    print l
    l.append(urllib.unquote('客户端'))
    print l
    for s in li:
        print s

from collections import namedtuple, Counter
def main():
    CoachLesson = namedtuple('CoachLesson', ['coach', 'learner', 'lesson_count']) # define a class
    list0 = ['Fred', 'A', 'A', 'B', 'C']
    coach0, learnerlist0 = str(list0[:1]), list0[1:]    # split input list
    #print coach, learner
    learnercount0 = Counter(learnerlist0)   # map for learner:count
    result = [CoachLesson(coach0, key, val) for key, val in count0.items()]
    print result

if __name__ == '__main__':
    #main()
    #print help(namedtuple)
    #test()
    print 37520453.0 / 1024 / 1024