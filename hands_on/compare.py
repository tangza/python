# encoding:utf-8

parent_path = "C:/Users/TANGZA/Desktop/Tasks/SCI task/"

def readlines(file_path):
    with open(file_path) as f:
        return [l.strip().replace(',', '') for l in f.readlines()]

def is_in_list(str, list):
    try:
        i = list.index(str)
        return i
    except:
        return -1

def main():
    #print readlines(parent_path+'temp.sql')
    ship_detail_l = readlines(parent_path+'temp.sql')
    po_abs_item_l = readlines(parent_path+'t.sql')
    miss_list = [s for s in ship_detail_l if is_in_list(s, po_abs_item_l) < 0]
    print '\n'.join(miss_list), '\nField count: ', len(miss_list)

if __name__ == '__main__':
    main()