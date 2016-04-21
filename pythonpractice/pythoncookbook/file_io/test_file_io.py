#! python
# encoding:utf-8

def test():
    with open("./test.txt", 'rt') as f, open("./result.txt", 'wt') as s:
        for i, line in enumerate(f, 1):
            s.write('insert into DIM_MS_NAME_SEQ VALUES ({}, {});\n'.format(i, line.strip()))


def main():
    test()

if __name__ == '__main__':
    main()