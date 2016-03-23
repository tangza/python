#! python
# encoding: utf-8
import os
#import subprocess

root_path = 'D:/share/sqlcutover/'

TNS_OLLRSPM = '''(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=hln2279p.oocl.com)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=ollrsprd.oocl)))'''

SCRIPTFILE = 0
DBNAME = 1
DBSCHEMA = 2
SEQUENCE = 3

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
    print 'sequence'.ljust(10), 'db'.ljust(20), 'schema'.ljust(30), 'script'
    for item in items:
        print str(item[3]).center(10), item[1].ljust(20), item[2].ljust(30), item[0]
    print str(len(items)).center(10), 'Exit'

def execute_item(item):
    file = ' @'+root_path+item[SCRIPTFILE]
    cmd = 'echo exit | sqlplus -S '+item[DBSCHEMA]+'/ollrspm@'+ TNS_OLLRSPM + ' @' + file
    #print cmd
    os.chdir(root_path)
    #os.system('cd')
    os.system(cmd)
    #subprocess.call(cmd)

def start():
    items = parse_parm(root_path)
    show_menu(items)
    while True:
        s = raw_input('Select item to cutover:')
        try:
            i = int(s)
            if i == len(items):
                print 'User select exit.'
                break
            if i < 0 or i > len(items):
                print 'Please select item from above menu!'
                continue
            execute_item(items[i])
        except :
            print 'Please input correct integer!'

    
if __name__ == '__main__':
    start()