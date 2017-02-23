# -*- coding: utf-8 -*-
import time
import datetime
import urllib
import re
import json

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_ip():
    c = getHtml('http://1212.ip138.com/ic.asp')
    d = unicode(c, 'gb2312').encode('utf-8')
    e = re.search('IP是：\[([\s\S]+?\])', d).group(1)
    ip = e[:-1]
    return ip

def get_ip_area(ip):
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
    content = urllib.urlopen(apiurl)
    testtest2 = content.read()
    testtest = json.loads(testtest2)
    return testtest

def get_weather(area):
    city = area['data']['city']
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=3f055ffd21e075647cbaa2f409ff737e' % city
    url = url.encode("utf-8")
    html = getHtml(url)
    a = json.loads(html)
    b = unicode(datetime.date.today())
    a1 = a['results'][0]['weather_data'][0]['date'] + a['results'][0]['weather_data'][0]['weather'] + \
         a['results'][0]['weather_data'][0]['wind'] + a['results'][0]['weather_data'][0]['temperature']
    weather=[]
    weather.append(a['results'][0]['currentCity'])
    weather.append(a1)
    weather.append(a['results'][0]['index'][0]['des'])
    for i in range(1,4):
        weather.append(a['results'][0]['weather_data'][i]['date'] + a['results'][0]['weather_data'][i]['weather'] + \
                       a['results'][0]['weather_data'][i]['wind'] + a['results'][0]['weather_data'][i]['temperature'])
    return weather

def start():
    ip = get_ip()
    area = get_ip_area(ip)
    weather = get_weather(area)
    return weather
