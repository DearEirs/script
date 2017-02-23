# -*- encoding: utf-8 -*-
import os
import threading
import re
from urllib import  urlopen
from urllib2 import Request,quote


def mkdir(filepath):
    #创建目录
    if not os.path.exists(filepath):
        try:
            os.mkdirs(r'%s' % filepath)
            msg = u'已创建目录,请查看%s' % filepath
            print msg
        except:
            os.mkdir(r'%s' % filepath)
            msg = u'已创建目录,请查看%s' % filepath
            print msg
    else:
        msg = u"目录已存在,现在开始爬去图片."
        print msg

def get_page(pages,threads):
    #传入1-100的页面数与开启线程数，返回list
    first_page,last_page = pages.split('-')
    first_page,last_page = int(first_page),int(last_page)
    sum_page = last_page-first_page+1
    thread = sum_page / threads
    thread_list = []
    for i in range(threads):
        if not i:
            thread_list.append(range(0,thread))
        else:
            thread_list.append(range(thread*i,thread*(i+1)))
    thread_list.append(range(thread*threads,last_page))
    return thread_list

def get_url(pages,key):
    key = quote(key)
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn={0}&word={1}'.format(pages*30,key)
    html = urlopen(url)
    html = html.read()
    imagesUrl = re.findall('objURL\W\W\Whttp:\/\/.*?\.png|objURL\W\W\Whttp:\/\/.*?\.jpe?g',html,re.IGNORECASE)
    realurl = re.findall("http:\/\/.*?\.png|http:\/\/.*?\.jpe?g",str(imagesUrl),re.IGNORECASE)
    a = []
    for i in realurl:
        if i[:6] == r'http://':
            a.append(i)
    realurl =  list(set(realurl).difference(set(a)))
    return  realurl

def down_img(page_list,filepath,key):
    for page_number in page_list:
        urls = get_url(page_number,key)
        for url in urls:
            filename = url.split('/')[-1]
            filename = filepath + '\\' + filename
            with open(filename, 'wb') as f:
                req = Request(url)
                req.add_header('user-agent',
                               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
                img = urlopen(url)
                img = img.read()
                f.write(img)
                f.close()
            print u'爬取图片%s成功！' % url

def input_threads():
    while True:
        threads = raw_input(u'请输入需要开启线程数,默认为5\r\n')
        if not threads:
            threads = 5
            break
        try:
            threads = int(threads)
            break
        except TypeError as e:
            print 'e'
            continue
    return threads

def input_page():
    while True:
        pages = raw_input(u'请输入需要爬取的页面数,如1-100\r\n')
        try:
            first,last = pages.split('-')
            try:
                int(first)
                int(last)
                break
            except:
                pass
        except:
            pass
        print u'页面数有误。'
    return pages

def main():
    print u'开始爬取百度图片^_^'
    filepath = raw_input(u'请输入图片存放路径.\r\n' )
    mkdir(filepath)
    key = raw_input(u'请输入关键字搜索。\r\n')
    pages = input_page()
    threads = input_threads()
    pages_list = get_page(pages,threads)
    for page_list in pages_list:
        down = threading.Thread(target=down_img,args=(page_list,filepath,key))
        down.start()

if __name__ == '__main__':
    main()

