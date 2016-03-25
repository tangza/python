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

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print ch

def test():
    from datetime import datetime, timedelta
    actual = datetime(2015, 4, 22)
    expect = datetime(2015, 1, 4)
    print expect - timedelta(days=21)

def main():
    #manual_iter()
    #test()
    test_iter_proxy()
    pass

if __name__ == '__main__':
    main()