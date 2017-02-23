# -*- coding: utf-8 -*-
import requests
import time
import datetime
import json
import urllib
import re
import sys
import chardet
import sys, os, urllib2, json
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
c = getHtml('http://1212.ip138.com/ic.asp')
d = unicode(c,'gb2312').encode('utf-8')
e = re.search('IP是：\[([\s\S]+?\])',d).group(1)
ip1 = e[:-1]
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
b = unicode(datetime.date.today())
a1 = a['results'][0]['weather_data'][0]['date'] + a['results'][0]['weather_data'][0]['weather'] + a['results'][0]['weather_data'][0]['wind'] + a['results'][0]['weather_data'][0]['temperature']
a2 = a['results'][0]['weather_data'][1]['date'] + a['results'][0]['weather_data'][1]['weather'] + a['results'][0]['weather_data'][1]['wind'] + a['results'][0]['weather_data'][1]['temperature']
a3 = a['results'][0]['weather_data'][2]['date'] + a['results'][0]['weather_data'][2]['weather'] + a['results'][0]['weather_data'][2]['wind'] + a['results'][0]['weather_data'][2]['temperature']
a4 = a['results'][0]['weather_data'][3]['date'] + a['results'][0]['weather_data'][3]['weather'] + a['results'][0]['weather_data'][3]['wind'] + a['results'][0]['weather_data'][3]['temperature']
for i in a['results']:
    if (time.strftime('%A')) == 'Monday':
        break
    if a['date'] == b:
        print i['currentCity']
        print a1
        print a['results'][0]['index'][0]['des']
if (time.strftime('%d')) == str(01) or (time.strftime('%A')) == 'Monday':
    print '新的一个月开始了,当前时间是：',b
if (time.strftime('%A')) == 'Monday':
    print '这周天气是：'
    print a1
    print a2
    print a3
    print a4
    print a2
    print a3
    print a4

'''
for i in a['results']:
    if (time.strftime('%A')) == 'Monday':
        break
    if a['date'] == b:
        print i['currentCity']
        print a1
        print a['results'][0]['index'][0]['des']
if (time.strftime('%d')) == str(01) or (time.strftime('%A')) == 'Monday':
    print '新的一个月开始了,当前时间是：', b
if (time.strftime('%A')) == 'Monday':
    print '这周天气是：'
    print a1
    print a2
    print a3
    print a4
'''



