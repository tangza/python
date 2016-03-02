def test():
    return lambda x: x * x
def test1():
    return power2
def power2(m):
    return m * m

print(test()(2))
print(test1()(2))
