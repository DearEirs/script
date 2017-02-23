#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libxml2
import requests
from lxml import etree
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

def req(url):
    parameters = {}
    req = requests.get(url, params=parameters)
    return (req.text,req.status_code)


def extract(htm, decoding, xpath):
    html = htm.decode(decoding)
    tree = etree.HTML(html)
    return tree.xpath(xpath)

def compurl(href):
    allpart = re.split('(\/\/)',href)
    protocol = ''.join(allpart[:2])
    addr = allpart[2]
    retlist = []
    retdict = {}
    source = {'esf':'esf.','newhouse':'newhouse.','zu':'zu.'}
    for x in source.values():
        ret = protocol + x + addr
        retlist.append(ret)
        #retdict['']
    return retlist


def catchid(htm):
    idlist = []
    sections = extract(htm,'utf-8','//*[@id="senfe"]/tbody/tr/@id')
    for id in sections:
        idlist.append(str(id))
        print id.text
    return idlist

def genid(num):
    idlist = []
    for x in range(1,num+1):
        if len(str(x)) <2:
            num = "0" + str(x)
            print num
            id = "sffamily_B03_%s" %num
            idlist.append(id)
        else:
            num = str(x)
            id = "sffamily_B03_%s" %num
            idlist.append(id)
    return idlist


if __name__ == '__main__':
    url = 'http://fang.com/SoufunFamily.htm'
    ret = req(url)
    #print ret[0]
    idlist = genid(30)
    print idlist
    dict1 = {}
    for id in idlist:
        urllist = []
        placelist = []
        xpath1 = '//*[@id="%s"]/td[3]/a' %id
        sections = extract(ret[0], 'utf-8',xpath1)
        for href in sections:
            #print str(href.text)
            placelist.append(href.text)
        print placelist
        xpath2 = '//*[@id="%s"]/td[3]/a/@href' %id
        print xpath2
        sections = extract(ret[0], 'utf-8',xpath2)
        for href in sections:
            #print str(href.text)
            urllist.append(href)
            print href
        print urllist
        for x,y in zip(placelist,urllist):
            print x,y
            dict1[str(x)] = compurl(y)
    print dict1
    print dict1['玉树']