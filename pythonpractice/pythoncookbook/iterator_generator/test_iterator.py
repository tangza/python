#! python
# encoding:utf-8

def manual_iter():
    with open('./test_iterator.py') as f:
        try:
            while True:
                line = next(f)
                print line,
        except StopIteration:
            pass
    #with open('test_iterator.py') as f:
    #    while True:
    #        line = next(f)
    #        if line is None:
    #            break
    #        print line,

def test_iter_proxy():
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                for c1 in c.depth_first():
                    yield c1

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print ch

def test_my_gen():
    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    for n in frange(0, 4, 0.5):
        print n

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reversed iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

def test_reversed_iter():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print x
    # with open('./test_iterator.py') as f:
    #     for line in reversed(list(f)):
    #         print line,
    for y in reversed(Countdown(10)):
        print y, ' ',
    print
    for y in Countdown(10):
        print y, ' ',

def test_derived_iter():
    from collections import deque
    class linehistory:
        def __init__(self, lines, histlen=3):
            self.lines = lines
            self.history = deque(maxlen=histlen)
        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):
                self.history.append((lineno, line))
                yield line
        def clear(self):
            self.history.clear()
    with open('./test_iterator.py') as f:
        lines = linehistory(f)
        # it = iter(lines)
        # next(it)
        next(iter(lines))
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print '{}:{}'.format(lineno, hline)

def test_slice():
    def count(n):
        while True:
            yield n
            n += 1
    c = count(0)
    import itertools
    for x in itertools.islice(c, 10, 15):
        print x

def test_dropwhile():
    from itertools import dropwhile
    with open('./test_iterator.py') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print line,

def test_permutation_combination():
    items = ['a', 'b', 'c']
    from itertools import permutations, combinations, combinations_with_replacement
    for p in permutations(items, 2):
        print p
    for c in combinations(items, 3):
        print c
    for c in combinations_with_replacement(items, 3):
        print c

def test_enumerate():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list, 1):
        print idx, val

def test_chain():
    from itertools import chain
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print x

def test_flatten():
    from collections import Iterable
    def flatten(items, ignore_type=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_type):
                for y in flatten(x):
                    yield y
            else:
                yield x
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    strs = ['Dave', 'Paula', ['Thomas', 'Lewis'], 'Paul']
    for x in flatten(strs):
        print x

def test_heapq():
    import heapq
    a = [1, 4, 7, 10]
    b = [2, 3, 5, 6, 11]
    for c in heapq.merge(a, b):
        print c

def test_iter_while():
    import sys
    for i in iter(lambda: raw_input(), ''):
        sys.stdout.write(i)


def test():
    from datetime import datetime, timedelta
    actual = datetime(2015, 4, 22)
    expect = datetime(2015, 1, 4)
    print expect - timedelta(days=21)


def main():
    #manual_iter()
    #test()
    # test_iter_proxy()
    # test_my_gen()
    # test_reversed_iter()
    # test_derived_iter()
    # test_slice()
    # test_dropwhile()
    # test_permutation_combination()
    # test_enumerate()
    # test_chain()
    # test_flatten()
    # test_heapq()
    test_iter_while()

if __name__ == '__main__':
    main()