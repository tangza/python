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
def main():
	test_class_string()

if __name__ == '__main__':
	main()