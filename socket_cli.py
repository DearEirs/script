#coding=gbk
import  socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.222.94',9090))
a = b'请输入英文名,退出请输入exit或quit'
print(a)

while 1:
    name = raw_input()
    if name:
        if name == 'exit' or name == 'quit':
            s.sendall(name)
            break
        s.sendall(name)
        number = s.recv(2048)
        print (number)
s.close()