#coding:utf-8
import socket
import threading
from time import sleep
'''
print "正在等待连接……"
while 1:
    sock, addr = s.accept()
    print "收到来自IP%s请求" % (addr[0])
    name = sock.recv(1024)
    print(1)
    users[addr] = ''
    if users[addr] not in users:
        users[addr] =name
        print(users)
    elif users[addr] != name:
        s.sendall('一个IP只能有一个用户名，请输入：',users[addr])
        print(users, 2)
    else:
        s.sendall('用户名已存在，请重新输入。')
        print(users, 3)
    print(users)
def response(sock, addr):
    data = sock.recv(1024)
    sock.sendall('%s:%s' % (users[addr[0]],data))
    sock.close()
    print('done')
 '''

def socke(sock, addr):
    while 1:
        data = sock.recv(1024)
        if 'first_time' in data:
            name = data[:data.index('first_time')]
            f = open(r'C:\Users\Dear\PycharmProjects\zuoye\users.txt','a+')
            user_data = str(addr[0])+'|'+str(addr[1])+'|'+name+'\r\n'
            f.write(user_data)
            f.close()
            sock.sendall('Welcome '+name+'!')
            continue
        else:
            all_data = name +':'+ data
            f = open(r'C:\Users\Dear\PycharmProjects\zuoye\users.txt', 'r')
            for i in  f.readlines():
                if i:
                    #if str(addr[0]) in i and str(addr[1]) in i:
                        #continue
                    #else:
                    ip,port,name = i.split('|')
                    print(ip,port,name)
                    a  = (ip,int(port))
                    sock.sendto(all_data,a)
            f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.153.215', 50007))
s.listen(50)

while 1:
    sock, addr = s.accept()
    t = threading.Thread(target=socke, args=(sock,addr))
    t.start()

def recv():
    while 1:
        print(sock.recv(1024).decode('utf-8'))

qq = threading.Thread(target=recv)

qq.start()















'''
import commands   #执行系统命令模块
HOST='10.0.0.245'
PORT=50007
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))   #套接字绑定的IP与端口
s.listen(1)         #开始TCP监听
while 1:
       conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
       print'Connected by',addr    #输出客户端的IP地址
       while 1:
                data=conn.recv(1024)    #把接收的数据实例化
                cmd_status,cmd_result=commands.getstatusoutput(data)   #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
                if len(cmd_result.strip()) ==0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
                        conn.sendall('Done.')
                else:
                       conn.sendall(cmd_result)   #否则就把结果发给对端（即客户端）
conn.close()     #关闭连接

'''