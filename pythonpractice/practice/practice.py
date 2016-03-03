# encoding: UTF-8
import re

def p():
	'''
	1. 编写代码, 打印1-1亿之内的偶数
	'''
	r = range(2, 100000000, 2)

def rege():
	'''
	2. 写一个函数, 用正则表达式清除字符串中[]和其中的内容
	'''
	s = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢"
	s = re.sub(r'\[.*?\]', '', s)
	print(s)

def desc():
	'''
	请使用python, 对下面的函数进行处理，
		def hello(name):
		    print "hello, %s" % name
	在函数被调用时打印耗时详情
		<function name: hello>
		<function call begin>
		hello, tom
		<function call end>
		[timecosts: 3.81469726562e-06s]
	'''
	import time
	import functools
	def log(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('<function name: %s>' % func.__name__)
			print('<function call begin>')
			time.clock()
			func(*args, **kw)
			print('<function call end>')
			print('[timecosts: %s' % time.clock())
		return wrapper

	@log
	def hello(name):
		print('hello, %s' % name)

	def printHello():
		hello('tom')
		print(hello.__name__)
	return printHello

def rename():
	'''
	4. 写一个函数, 将驼峰命名法字符串转成下划线命名字符串(需考虑各类编码中常见的命名)
		GetItem -> get_item
      	getItem -> get_item
      	doIT    -> do_IT

	'''
	def camelToUnderscode(names):
		import re
		result = []
		pattern = re.compile(r'([A-Z]{1,}[a-z]{0,})|([a-zA-Z][a-z]{0,})')
		for name in names:
			match = pattern.findall(name)
			if match:
				l = []
				for s in match:
					s = ''.join(s)
					if s.isupper():
						l.append(s)
					else:
						l.append(s.lower())
				result.append('_'.join(l))
		return result
	def test():
		print(camelToUnderscode(['GetItem', 'getItem', 'doIT', 'isItGood']))

	return test
# rege()
# desc()()
rename()()