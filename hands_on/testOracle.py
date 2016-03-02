import cx_Oracle

conn = cx_Oracle.connect('HLLP_SCISP_ADMIN', 'HLLPSCISPADMIN', '(DESCRIPTION =(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = hkln832p)(PORT = 1521)) )    (CONNECT_DATA =      (SERVICE_NAME = ollrptqa.oocl)    )  )')
# conn = cx_Oracle.connect( "ivo_aesupp", "ivoaesupp","(DESCRIPTION =    (ADDRESS_LIST =      (ADDRESS = (PROTOCOL = TCP)(HOST = hklxdv41)(PORT = 1521))    )    (CONNECT_DATA =      (SERVICE_NAMES = ivosit.oocl)      (SID = ivosit)    )  )  ")
# conn = cx_Oracle.connect()
cursor = conn.cursor()
cursor.execute('select * from DIM_CUST_SETTING')
rows = cursor.fetchall()
print(len(rows))
for row in rows:
    for field in row:
        print(field),
    print('')
cursor.close()
conn.close()