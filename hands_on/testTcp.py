# encoding: UTF-8

from socket import *

HOST = 'hkln218p'
PORT = 17427
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)
#while True:
print('Connect succeeded')
data = tcpClientSock.send('show')
print(data)
tcpClientSock.close()