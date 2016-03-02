import cx_Oracle

OLRS_QA_TNS = '(DESCRIPTION =(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = hkln832p)(PORT = 1521)) )    (CONNECT_DATA =      (SERVICE_NAME = ollrptqa.oocl)    )  )'

OLRS_PRD_TNS = '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=ollrsdbprd)(PORT=1521)))(CONNECT_DATA=(SID=ollrsprd)))'
OLRS_PRD_RPTSUPP_USERNAME = 'HLLP_RPT_SUPP'
OLRS_PRD_RPTSUPP_PASSWORD = 'temp'
OLRS_PRD_SCISUPP_USERNAME = 'HLLP_SCI_SUPP'
OLRS_PRD_SCISUPP_PASSWORD = 'hllpscisuppprd'
OLRS_PRD_DWSUPP_USERNAME = 'ORSPOD_DW_SUPP'
OLRS_PRD_DWSUPP_PASSWORD = 'orspoddwsupp'

SQL_CHECK_RPT_JOB_STATUS = '''
    SELECT distinct case
              when sysdate - (1 / 24 / 60) * 6 > start_process_time then
               'TRUE'
              else
               'FALSE'
            end is_shut_down
    FROM rpt_process_log
    WHERE refresh_job_id IN
       (SELECT last_process_job
          FROM rpt_refresh_status
         where process_name = 'PROC_STG_LLP_PO')
'''
SQL_CHECK_SCI_JOB_STATUS = '''
    select decode(sum(case
                    when from_proc like 'START%' then
                     1
                    else
                     -1
                  end),
              0,
              'Stoped',
              'Runing') status
    from sci_process_log t
    where (t.from_proc like 'END%' OR t.from_proc LIKE 'START%')
    and t.from_proc <> 'START SCI EXCEPTION ETL'
    and t.crtdate > sysdate - (1 / 24 / 60) * 90
    and t.REFRESH_JOB_ID =
       (select max(REFRESH_JOB_ID)
          from sci_process_log t2
         where (t2.from_proc like 'END%' OR t2.from_proc LIKE 'START%')
           and t2.from_proc <> 'START SCI EXCEPTION ETL'
           and t2.crtdate > sysdate - (1 / 24 / 60) * 90
           and t2.module_name = t.module_name)
'''

conn = cx_Oracle.connect(OLRS_PRD_SCISUPP_USERNAME, OLRS_PRD_SCISUPP_PASSWORD, OLRS_PRD_TNS)
# conn = cx_Oracle.connect( "ivo_aesupp", "ivoaesupp","(DESCRIPTION =    (ADDRESS_LIST =      (ADDRESS = (PROTOCOL = TCP)(HOST = hklxdv41)(PORT = 1521))    )    (CONNECT_DATA =      (SERVICE_NAMES = ivosit.oocl)      (SID = ivosit)    )  )  ")
cursor = conn.cursor()
# cursor.execute('select * from DIM_CUST_SETTING')
def execute_print(sql):
    cursor.execute(sql)
    rows = cursor.fetchall()
    # print(len(rows))
    for row in rows:
        for field in row:
            print(field),
        print('')

execute_print(SQL_CHECK_RPT_JOB_STATUS)
execute_print(SQL_CHECK_SCI_JOB_STATUS)

cursor.close()
conn.close()