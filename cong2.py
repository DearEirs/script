# -*- encoding: utf-8 -*-
import os
import re
from urllib import  urlopen
from urllib2 import Request
import threading
import time
def get_page(pages):
    first_page,last_page = pages.split('-')
    first_page,last_page = int(first_page),int(last_page)
    sum_page = last_page-first_page+1
    if sum_page < 20:
        threads = 3
    else:
        threads = 10
    thread = sum_page / threads
    thread_list = []
    others = sum_page % threads
    for i in range(threads):
        if not i:
            thread_list.append(range(0,thread))
        else:
            thread_list.append(range(thread*i,thread*(i+1)))
    #thread_list.append(range(thread*threads,last_page))
    return thread_list

'''
def get_page(pages):
    first_page, last_page = pages.split('-')
    first_page, last_page = int(first_page), int(last_page)
    page_num = last_page - first_page
    if page_num < 10 :
        threads = 3
    else:
        threads = 5
    page = range(first_page,last_page+1)

    le = page_num / threads
    p_list = []
    for i in range(threads):
        if not i:
            p_list.append(range(first_page,first_page+le))
        else:
            p_list.append(range(first_page+(le*i),first_page+(le*(i+1))))
        if first_page+(le*(i+1)) !=  last_page:
            p_list.append(range(first_page+(le*(i+1)),last_page))
    return p_list
'''
pages_url = []
def get_page_url(page):
    for i in page:
        if i == 1 or i ==0:
            url = 'http://1122ig.com/tupianqu/siwa/index.html'
            pages_url.append(url)
        else:
            url = 'http://1122ig.com/tupianqu/siwa/index_%s.html' % i
            pages_url.append(url)
    return pages_url

def get_img_url(page_url):
    p_url = []
    for url in page_url:
        html = urlopen(url)
        html = html.read()
        pa_url = re.findall('\/tupianqu\/siwa\/\d+\.html',html)
        img_html = urlopen(page_url)
        img_html = img_html.read()
        img_html = re.findall('http\W\/\/cache3\.onlyimg\.com\/pics\/\d+\.jpg', img_html)
        p_url.append(pa_url)
    print  p_url
    img_url =[]
    for url in p_url:
        url = r'www1122ig.com{0}'.format(url)
        html =urlopen(url)
        html = html.read()
        img_url.append(re.findall('http\W\/\/cache3\.onlyimg\.com\/pics\/\d+\.jpg', html))
    return img_url

def down_img(page):
    page_url = get_page_url(page)
    img_url = get_img_url(page_url)
    for url in img_url:
        filename = url.split('/')[-1]
        filename = r'D:\img' + '\\' + filename
        with open(filename, 'wb') as f:
            req = Request(url)
            req.add_header('user-agent',
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
            img = urlopen(url)
            img = img.read()
            f.write(img)
            f.close()


def main():
    pages = raw_input()
    pages = get_page(pages)
    for page in pages:
        down = threading.Thread(target=down_img, args=(page,))
        down.start()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
