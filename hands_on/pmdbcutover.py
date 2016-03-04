#! python
# encoding: utf-8
import os

root_path = 'D://share/sqlcutover/'

OLLRSPM = '''(DESCRIPTION=(ADDRESS = (PROTOCOL = TCP)(HOST = hln2279p.oocl.com)(PORT = 1521))(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = ollrsprd.oocl)))'''

def parse_parm(path):
    items = []
    with open(path + 'apply.parm', 'r') as f:
        lines = f.readlines()
        seq = 0
        for line in lines:
            l = line.strip().split(' ')
            l.append(seq)
            seq += 1
            #print tuple(l)
            items.append(tuple(l))
    #print items
    return items

def show_menu(items):
    print 'sequence\t', 'db\t\t\t', 'schema\t\t\t\t\t', 'script\t'
    for item in items:
        print item[3], '\t\t', item[1], '\t\t', item[2], '\t\t', item[0]
    print len(items), '\t\t', 'Exit'

def execute_item(item):
    print 'executing ', item
    cmd = 'sqlplus '+item[2]+'/ollrspm@'+ '//hln2279p.oocl.com:1521/ollrsprd.oocl' + ' @'+root_path+item[0]
    print cmd
    os.system(cmd)

def start():
    items = parse_parm(root_path)
    show_menu(items)
    while True:
        s = raw_input('Select item to cutover:')
        i = int(s)
        if i < 0 or i >= len(items):
            break
        execute_item(items[i])

    
if __name__ == '__main__':
    start()