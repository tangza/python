from email.mime.text import MIMEText

msg = MIMEText('Hello, this message is sent from Python!', 'plain', 'utf-8')

# Email地址和口令：
# from_addr = input('From: ')
# from_addr = 'cabernaster@sina.com'
from_addr = ''
password = input('Password: ')
print(password)

# 收件人地址：
# to_addr = input('To: ')
# to_addr = '1321514379@qq.com'
to_addr = 'cabernaster@sina.com'

# SMTP Server address:
# smtp_server = input('SMTP server: ')
# smtp_server = 'smtp.sina.com'
smtp_server = 'testsmtp3'

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP protocal's default port is 25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
