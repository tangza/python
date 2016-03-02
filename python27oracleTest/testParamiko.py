import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('hkln604p', port=22, username='podiumco', password='podiumco2012')
stdin, stdout, stderr = client.exec_command('df | grep podium')
# stdin, stdout, stderr = client.exec_command('cd ./scripts;pwd')
for line in stdout:
    if not 'demo' in line.lower():
        print '...' + line.strip('\n')
client.close()
