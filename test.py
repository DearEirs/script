#conding:utf8
'''
import requests
import time

url = 'http://192.168.38.50/kh6/Login.aspx'

data = {
    'txtId' : '9999',
    'txtPwd' : 'admincrm@2013',
}
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}
s = requests.session()

response = requests.post(url=url,data=data,headers=header)
print 1
html = requests.get('http://192.168.38.50/kh6/Employees.aspx',headers=response.headers).text
print 2
print html
'''

'''
import traceback
x = 0
c = []
d = {}
d['start'] = 0
def jump(start,end,x=0):
    x += 1
    if d['start'] >= x :
        return
    else:
        d['start'] = x
    a = [i for i in range(2, start) if start % i == 0]
    for i in a:
        start_num = start + i
        if start_num == end :
            c.append(x)
        elif start_num > end:
            pass
        elif start_num < end:
            jump(start_num,end,x=x)
try:
    jump(10,30)
    c.sort()
    print c[0]
except:
    traceback.print_exc()

'''



'''
class Node(object):
    def __init__(self,start=None,left=None,right=None,end=None):
        self.value = start
        self.left = left
        self.right = right

if __name__ == '__main__':
    root = Node(4)
'''

'''
import pygame
import os

#os.system(r"C:\Users\Dear\Music\Eisblume.mp3")
a = os.stat(r"C:\\Users\\Dear\\Music\\Hans.mp3")
b = os.stat(r"C:\\Users\\Dear\\Music\\Eisblume.mp3")
print a
print b
'''

import xlrd

data = xlrd.open_workbook(r'D:\1.xlsx')
table =  data.sheets()[0]
print table.row_values(1)