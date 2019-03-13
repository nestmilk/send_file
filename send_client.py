# _*_ coding: utf-8 _*_
__author__ = 'nestmilk'
__date__ = '2019/3/12 12:51'

import socket

sk= socket.socket()

ip_port = ('192.168.1.8', 9999)

sk.connect(ip_port)

with open('D:\\text.txt', 'rb') as f:
    for i in f:
        sk.send(i)
        data = sk.recv(1024)
        if data == 'success':
            continue

sk.send('quit')
