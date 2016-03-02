import sqlite3

def createTable():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user(id, name) values (\'1\', \'Zack\')')

    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

def searchTable():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        cursor.execute('select * from user where id=?', '1')

        values = cursor.fetchall()
        # print(values)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return values

print(searchTable())