# encoding: UTF-8
import re

def hi():
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r'(?i)(?P<s>.*?hi)')

    # 使用Pattern匹配文本，获取匹配结果，无法匹配将返回None
    match = pattern.match(' hi, all!Hi')

    if match:
        # 使用Match获取分组信息
        print(match.group())
        print(match.groupdict())
        print(match.group('s'))
        print(match.span())
        print(match.expand(r'\g<s> all of you!'))

def testMatch():
    #import re
    m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
    
    print "m.string:", m.string
    print "m.re:", m.re
    print "m.pos:", m.pos
    print "m.endpos:", m.endpos
    print "m.lastindex:", m.lastindex
    print "m.lastgroup:", m.lastgroup
    
    print "m.group(1,2):", m.group(1, 2)
    print "m.groups():", m.groups()
    print "m.groupdict():", m.groupdict()
    print "m.start(2):", m.start(2)
    print "m.end(2):", m.end(2)
    print "m.span(2):", m.span(2)
    print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

def testPattern():
    p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
    
    print "p.pattern:", p.pattern
    print "p.flags:", p.flags
    print "p.groups:", p.groups
    print "p.groupindex:", p.groupindex

testMatch()
testPattern()