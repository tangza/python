#! python
# encoding:utf-8

def test_variable_length_func():
	# variable length position arguments
	def avg(first, *rest):
		return 1.0 * (first + sum(rest)) / (1 + len(rest))
	print avg(1, 2)
	print avg(1, 2, 3)

	import html, cgi
	# variable length key-value arguments
	def make_element(name, value, **attrs):
		keyvals = [' %s="%s"' % item for item in attrs.items()]
		attr_str = ''.join(keyvals)
		element = '<{name}{attrs}>{value}</{name}>'.format(
					name=name,
					attrs=attr_str,
					value=cgi.escape(value))
		return element
	print make_element('item', 'Albatross', size='large', quantity=6)
	print make_element('p', '<spam>')

	def anyargs(*args, **kwargs):
		print args
		print kwargs
	anyargs(1, 'hi', a=2, b='ok')

def test_annotations():
	# def add(x: int, y: int) -> int:	in python3
	# in python2.7 not supported, use comment instead
	# type: (int, int) -> int
	def add(x, y):
		return x + y
	print help(add)

def test_return_multiple():
	def myfun():
		return 1, 2, 3
	a, b, c = myfun()
	print a, b, c

def test_default_param():
	x = 1
	def spam(a, b=x):
		print a, b
	spam(1)
	x = 2
	spam(1)

	_no_value = object()
	def best_spam_practise(a, b=_no_value):
		if b is _no_value:
			print 'No b value supplied'
			return
		print a, b
	best_spam_practise('hi')
	best_spam_practise('hi', 'yes')

def test_lambda():
	funcs = [lambda x: x+n for n in range(5)]
	for f in funcs:
		print f(0)
	funcs1 = [lambda x, n=n: x+n for n in range(5)]
	for f in funcs1:
		print f(0)

def main():
	# test_variable_length_func()
	# test_annotations()
	# test_return_multiple()
	# test_default_param()
	test_lambda()

if __name__ == '__main__':
	main()