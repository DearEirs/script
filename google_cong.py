# -*- encoding: utf-8 -*-

import os
from urllib2 import urlopen,quote,Request
from urlparse import urljoin,urlparse,urlunparse
import threading
from lxml import etree
import  requests
import  sys

reload(sys)
sys.setdefaultencoding('utf-8')

def req(url):
    parameters = {}
    req = requests.get(url, params=parameters)
    return req.text,req.status_code

def extract(htm, decoding, xpath):
    html = htm.decode(decoding)
    tree = etree.HTML(html)
    return tree.xpath(xpath)

def getdata(key):
    key = quote(key)
    url = 'https://www.google.com.hk/search?safe=strict&site=&source=hp&q=python&oq=python'
    ret = req(url)
    print ret
    # req = Request(url)
    # req.add_header('user-agent',
    #                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    # html = urlopen(url)
    # html = html.read()
    # print html
    #print ret
    xpath1 = '//div[@class="rc"]'
    #title = extract(ret,'utf-8',xpath1)
    #return  title



key = u'东莞'
title = getdata('key')
print title
url = 'https://www.google.com.hk/?gws_rd=cr,ssl#q=%E4%B8%9C%E8%8E%9E&newwindow=1&safe=strict&start=10'