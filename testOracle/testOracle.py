import cx_Oracle

conn = cx_Oracle.connect('HLLP_SCISP_ADMIN', 'HLLPSCISPADMIN', 'DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=ollrptdbqa)(PORT=1521)))(CONNECT_DATA=(SID=ollrptqa))')
cursor = conn.cursor()
cursor.execute('select * from dual')
row = cursor.fetchone()
print(row[0])

cursor.close()
conn.close()