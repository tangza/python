#! python
# encoding:utf-8

def test():
    with open("./test.txt", 'rt') as f, open("./result.txt", 'wt') as s:
        for i, line in enumerate(f, 1):
            s.write('insert into DIM_MS_NAME_SEQ VALUES ({}, {});\n'.format(i, line.strip()))

import re
def get_artifact():
    with open('./test.txt', 'rt') as inf, open('./result.txt', 'wt') as outf:
        p = re.compile(r'\s*<artifactId>(.*)</artifactId>\s*')
        for l in inf:
            match = p.search(l)
            if match:
                #print match.group(1)
                art = match.group(1)
                outf.write(art + '\n')

def in_file(f, s):
    f.seek(0)
    for l in f.readlines():
        if l.find(s) != -1:
            print s
            return True
    return False

def check_exist():
    with open('./result.txt', 'a+t') as f, open('./test1.txt', 'rt') as rf:
        for l in f.readlines():
            print l
            if in_file(rf, l.strip()):
                f.write(l.strip() + '\t' + 'Y' + '\n')
            else:
                f.write(l.strip() + '\t' + 'N' + '\n')

from collections import Counter
def get_jar():
    with open('D:/Tasks/mvndepen.xml', 'rt') as inf, open('./test1.txt', 'wt') as outf, open('./result.txt', 'wt') as rf:
        p = re.compile(r'^\[INFO\].*- ([a-zA-Z0-9.:-_]*)$')
        c = Counter()
        for l in inf:
            #print l
            match = p.match(l)
            if match:
                #print match.group(1)
                r = match.group(1)
                c[r] += 1
                rl = r.split(':')
                jar, version = ':'.join(rl[:3]), ':'.join(rl[3:])
                outf.write(jar + ' -- ' + version + '\n')
        sc = sorted(c.items())
        for k, v in sc:
            rf.write(k + ' -- ' + str(v) + '\n')

def get_mif_conf():
    with open('D:/Tasks/mifReceiver.xml', 'rt') as inf, open('./test1.txt', 'wt') as outf:
        p = re.compile(r'(?.)\s+<receiver:message type="(\w+)">\n\s+<receiver:version value="(ver1.0)">\n\s+<receiver:app receiverId="\w+">\n')
        l = inf.read()
        match = p.match(l)
        if match:
            r = match.groups()
            print r

from ConfigParser import ConfigParser
def gen_ems_config():
    with open('result.txt', 'wt') as outf:
        cf = ConfigParser()
        cf.read('test.ini')
        #cf.sections()
        #print cf.options('Queue')
        outf.write('create user ips_user\n')
        outf.write('set password ips_user ips_user\n')
        for (k, v) in cf.items('Queue'):
            outf.write('create queue ' + v + ' secure\n')
            outf.write('grant queue ' + v + ' user=ips_user all\n')
        outf.write('\n')
        for (k, v) in cf.items('Topic'):
            outf.write('create topic ' + v + ' global,secure\n')
            outf.write('grant topic ' + v + ' user=ips_user all\n')



def main():
    #test()
    #print help(re)
    #get_artifact()
    #check_exist()
    #get_jar()
    gen_ems_config()
    #print help(ConfigParser)

if __name__ == '__main__':
    main()