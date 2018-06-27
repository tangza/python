#! python2
# encoding:utf-8

def test_class_string():
	class Pair:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def __repr__(self):
			return 'Pair({0.x!r}, {0.y!r})'.format(self)
		def __str__(self):
			return '({0.x!s}, {0.y!s})'.format(self)
	p = Pair(3, 4)
	print p
	print repr(p)

def test_context():
    class MyContext(object):
        def __init__(self):
            print 'initial context'
        def __enter__(self):
            print 'enter context...'

        def __exit__(self, exc_ty, exc_val, tb):
            print 'exit context...'

    with MyContext() as con:
    	print 'using context...'
        print MyContext.__mro__
def main():
	# test_class_string()
	test_context()

if __name__ == '__main__':
	main()