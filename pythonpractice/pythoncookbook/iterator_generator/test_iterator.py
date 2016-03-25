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

def test():
    from datetime import datetime, timedelta
    actual = datetime(2015, 4, 22)
    expect = datetime(2015, 1, 4)
    print expect - timedelta(days=21)

def main():
    #manual_iter()
    test()
    pass

if __name__ == '__main__':
    main()