#coding=gbk
import socket
import threading
import MySQLdb

def getnumber(name,ip,data_type):
    conn = MySQLdb.connect(host='%s' % ip, user='root', passwd='both-win', db='asterisk', port=3306)
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    par = '%'+name+'%'
    sql = "select  name,extension from users where %s like %s;" % data_type,par
    cur.execute(sql,par)
    select = cur.fetchall()
    result=''
    if select:
        for i in range(0,len(select)):
            name = select[i]['name']
            extension = select[i]['extension']
            result = result+ name +"   " +extension +'\r\n'
    conn.close()
    return result
def getallnumber(name,ip,data_type):
    result = ''
    for i in ip:
        result = result + getnumber(name,i,data_type)
    if not result:
        result = b'找不到相关分机'
    return  result

def tcplink(sock,addr,ip):
    while 1 :
        data = sock.recv(1024)
        try:
            data = int(data)
            data_type = 'extension'
        except:
            if data == 'exit' or data =='quit':
                data_type = 'name'
                sock.close()
                break
            else:
                number = getallnumber(data,ip,data_type)
                sock.send(number)
ip=['192.168.38.200','192.168.38.254','192.168.60.200','192.168.65.200']
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.222.94', 9090))
s.listen(30)
while 1:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock,addr,ip))
    t.start()
