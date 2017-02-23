# -*- encoding: utf-8 -*-
import re
from urllib import  urlopen
from urllib2 import Request
from urlparse import urljoin
import threading
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
    return thread_list

def down(pages):
    for page in pages:
        if page == 1 or page ==0:
            url = 'http://1122ig.com/tupianqu/yazhou/index.html'
        else:
            url = 'http://1122ig.com/tupianqu/yazhou/index_%s.html' % page
        page_html = urlopen(url)
        page_html = page_html.read()
        pages_url = re.findall('\/tupianqu\/yazhou\/\d+\.html', page_html)
        for page_url in  pages_url:

            head = r'http://www.1122ig.com'
            page_url = urljoin(head,page_url)
            img_html = urlopen(page_url)
            img_html = img_html.read()
            imgs_url = re.findall('http\W\/\/cache3\.onlyimg\.com\/pics\/\d+\/\d+\.jpg', img_html)
            print imgs_url
            for img_url in imgs_url:
                print(img_url)
                filename = img_url.split('/')[-1]
                filename = r'C:\Users\Administrator\Desktop' + '\\' + filename
                with open(filename, 'wb') as f:
                    req = Request(url)
                    req.add_header('user-agent',
                                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
                    img = urlopen(img_url)
                    img = img.read()
                    f.write(img)
                    f.close()

def main():
    page_number = "1-100"
    pages = get_page(page_number)
    for i in pages:
        t = threading.Thread(target=down,args=(i,))
        t.start()
if __name__ == '__main__':

    main()