#! python
#encoding:utf-8

# print 'hi'
def test_round():
	print round(1.5)
	print round(3.14159, 2)
	print round(3.14159, 3)
	print round(31.4159, -1)

def test_decimal():
	# use decimal module to perform accurate decimal calculations
	from decimal import Decimal
	a = Decimal('4.2')
	b = Decimal('2.1')
	c = 4.2
	d = 2.1
	print a+b, (a+b) == Decimal('6.3')
	print c+d, (c+d) == 6.3
	from decimal import localcontext
	e = Decimal('1.3')
	f = Decimal('1.7')
	print e/f
	with localcontext() as ctx:
		ctx.prec = 3
		print e/f
	with localcontext() as ctx:
		ctx.prec = 50
		print e/f
	nums = [1.23e+18, 1, -1.23e+18]
	print sum(nums)
	import math
	print math.fsum(nums)

def test_format():
	x = 1234.56789
	print format(x, '0.2f')
	print format(x, '>10.1f')
	print format(x, '<10.1f')
	print format(x, '^10.1f')
	print format(x, ',')
	print format(x, '0,.1f')
	print format(x, 'e')
	print format(x, '0.2E')
	print 'The value is {:0,.2f}'.format(x)

def test_bin_hex_oct():
	x = 1234
	print bin(x)
	print format(x, 'b')
	print oct(x)
	print format(x, 'o')
	print hex(x)
	print format(x, 'x')
	y = -1234
	print format(y, 'b')
	print format(2**32 + y, 'b')
	print format(2**32 + y, 'x')
	print int('4d2', 16)
	print int('10011010010', 2)
	print int('44', 5)
	print 0o755

def test_from_to_bytes():
	data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
	print(len(data))
	# print(int.from_bytes(data, 'little'))
	# print(int.from_bytes(data, 'big'))
	x = 94522842520747284487117727783387188
	# print(x.to_bytes(16, 'big'))
	# print(x.to_bytes(16, 'little'))
	import struct
	hi, lo = struct.unpack('>QQ', data)
	print (hi<<64) + lo
	print x.bit_length()
	y = 523 ** 23
	print y
	print y.bit_length()
	nbytes, rem = divmod(y.bit_length(), 8)
	if rem:
		nbytes += 1
	print nbytes, rem
	# print(y.to_bytes(nbytes, 'little'))

def test_complex():
	a = complex(2, 4)
	b = 3 - 4j
	print a
	print b
	print a.real
	print a.imag
	print a.conjugate()
	print a + b
	print a * b
	print a / b
	print abs(b)
	import cmath
	print cmath.sin(a)
	print cmath.cos(b)
	print cmath.exp(a)
	print cmath.sqrt(-1)

def test_nan():
	a = float('inf')
	b = float('-inf')
	c = float('nan')
	print a
	print b
	print c
	import math
	print math.isinf(a) & math.isinf(b)
	print math.isnan(c)
	d = a + b
	print d
	print d is c
	print d == c

def test_fractions():
	from fractions import Fraction
	a = Fraction(5, 4)
	b = Fraction(7, 16)
	print a + b
	print a * b
	c = a * b
	print c.numerator
	print c.denominator
	print float(c)
	print c.limit_denominator(8)
	x = 3.75
	y = Fraction(*x.as_integer_ratio())
	print y

def test_array():
	x = [1, 2, 3, 4]
	y = [5, 6, 7, 8]
	print x * 2
	print x + y

	import numpy as np
	ax = np.array([1, 2, 3, 4])
	ay = np.array([5, 6, 7, 8])
	print ax * 2
	print ax + 10
	print ax + ay
	print ax * ay
	print (lambda a : 3*a**2 - 2*a + 7)(ax)
	print np.sqrt(ax)
	print np.cos(ax)
	grid = np.zeros(shape=(10, 10), dtype=float)
	grid += 10
	# print grid
	# print np.sin(grid)
	a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
	print a
	print a[1]
	print a[:,1]
	print a[1:3, 1:3]
	a[1:3, 1:3] += 10
	print a
	print a + [100, 101, 102, 103]
	print np.where(a < 10, a, 10)

def test_matrix():
	import numpy as np
	m = np.matrix([[1,-2,3], [0,4,5], [7,8,-9]])
	print m
	print m.T
	print m.I
	v = np.matrix([[2],[3],[4]])
	print v
	print m * v

	import numpy.linalg
	# Determinant
	print numpy.linalg.det(m)
	# Eigenvalue
	print numpy.linalg.eigvals(m)
	# Solve for x in mx = v
	x = numpy.linalg.solve(m, v)
	print x
	print m * x

def test_random():
	import random
	# random.seed(b'byte')
	values = [1, 2, 3, 4, 5, 6]
	print random.choice(values)
	print random.sample(values, 2)
	# print random.shuffle(values)
	print values
	print random.randint(0, 10)
	print random.random()
	print random.getrandbits(10)
	print random.uniform(0, 1)
	print random.gauss(0, 1)


def main():
	# test_round()
	# test_decimal()
	# test_format()
	# test_bin_hex_oct()
	# test_from_to_bytes()
	# test_complex()
	# test_nan()
	# test_fractions()
	# test_array()
	# test_matrix()
	test_random()

if __name__ == '__main__':
	main()