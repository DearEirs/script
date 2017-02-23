#coding=utf-8
import socket
import requests
import time
import datetime
import json
import urllib,threading
import re
import sys
import chardet
import sys, os, urllib2, json,sys
reload(sys)

code = sys.getdefaultencoding()
sys.setdefaultencoding('%s' % code)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9090))
print code
print (s.recv(2048).decode('utf-8'))
name = raw_input('请输入一个昵称：')
name1 = name + str('first_time')
s.sendall(name1)
def recv():
    while True:
        print (s.recv(1024).decode('utf-8'))
t = threading.Thread(target=recv)
t.start()
while True:
    a = raw_input('请输入聊天内容:')
    if a == '':
        print '不能为空，请重新输入：'
        continue
    elif a == '-h':
        print '-show_member:查看当前在线用户 -datetime:查看当前时间-weather:查看当前天气 "exit"退出聊天室'
    elif a == 'exit':
        s.send(b'exit')
        break
    elif a == '-datetime':
        print time.strftime('%Y-%m-%d %H:%M:%S')
    elif a == '-weather':
            def getHtml(url):
                 page = urllib.urlopen(url)
                 html = page.read()
                 return html
            c = getHtml('http://1212.ip138.com/ic.asp')
            d = unicode(c,'gb2312').encode('utf-8')
            e = re.search('IP是：\[([\s\S]+?\])',d)
            f = e.group(1)
            ip1 = f[:-1]
            def get_ip_area(ip):
                apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" %ip
                content = urllib.urlopen(apiurl)
                testtest2 = content.read()
                testtest = json.loads(testtest2)
                return testtest
            test = get_ip_area(ip1)
            test1 = test['data']['city']
            haha = 'http://api.map.baidu.com/telematics/v3/weather?location='
            hehe = '&output=json&ak=3f055ffd21e075647cbaa2f409ff737e'
            url1 = haha + test1 + hehe
            url1 = url1.encode("utf-8")
            html  = getHtml(url1)
            a = json.loads(html)
            c = a['results'][0]['weather_data'][0]['weather'] + a['results'][0]['weather_data'][0]['wind'] + a['results'][0]['weather_data'][0]['temperature']
            print c
    else:
        s.send(a)