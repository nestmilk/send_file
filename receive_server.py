# _*_ coding: utf-8 _*_
import socket

__author__ = 'nestmilk'
__date__ = '2019/3/12 13:21'


sk = socket.socket()

#哈哈哈 版本2
ip_port = ('192.168.1.8', 9999)

sk.bind(ip_port)

sk.listen(5)

while True:
    conn, address = sk.accept()
    while True:
        with open('D:\p.txt','ab') as f:
            data = conn.recv(1024)
            if data == 'quit':
                break
            f.write(data)
        conn.send('success')

sk.close()