# -*- encoding: utf-8 -*-
import os
import re
#from urllib import  urlopen
from urllib2 import Request,urlopen
from urlparse import urljoin,urlparse,urlunparse
import threading
import time
'''
def down(number):
    url ='http://120.52.73.61/data1.cache.directory/media/videos/iphone/8%s.mp4' % number
    filename = r'D:\video\%s.mp4' % number
    with open(filename,'wb') as f:
        req = Request(url)
        req.add_header('user-agent',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
        img = urlopen(url)
        img = img.read()
        f.write(img)
        f.close()

for i in range(90,95):
    t = threart()
'''


number_list = []
head ='http://1199av.net'
for i in range(2,8):
    url = 'http://1199av.net/list/10-%s.html' % i
    html = urlopen(url)
    html = html.read()
    page_url = re.findall('\/vod\/\d+\.html', html)
    page_url = list(set(page_url))
    for i in page_url:
        i = urljoin(head, i)
        try:
            html = urlopen(i)
        except:
            print i, 'timeout'
            continue
        html = html.read()
        js_url = re.findall('\/vod\/\d+\Wplay\W\d+\W', html)
        js_url[0] += '0-1.js'
        number_url = urljoin(head, js_url[0])
        html = urlopen(number_url)
        html = html.read()
        number = re.findall('\d+\"\;$', html)
        number = number[0][:-2]
        number_list.append(number)
        print number_list


def down(numbers):
    for number in numbers:
        down_url = 'http://120.52.73.61/data1.cache.directory/media/videos/iphone/%s.mp4' % number
        filename = r'D:\video' + '\\' + number + '.mp4'
        with open(filename, 'wb') as f:
            req = Request(down_url)
            req.add_header('user-agent',
                           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
            video = urlopen(down_url)
            print down_url
            video = video.read()
            f.write(video)
            f.close()
try:
    os.mkdir(r'D:\video')
except:
    print r'D:\video is already exit.'
#number_list = ['1190', '894', '1202', '2718', '1211', '1201', '1200', '1209', '912', '2721', '1194', '904', '903', '1203', '4288', '4347', '896', '4321', '4286', '4336', '4344', '913', '2738', '2726', '4355', '4255', '4233', '4281', '4168', '4059', '4042', '4035', '4046', '4037', '4250', '4019', '4029', '4296', '4117', '4015', '4057', '4308', '4141', '3901', '4116', '3921', '4142', '3983', '4146', '3906', '4139', '4114', '3884', '4140', '4123', '4101', '4297', '4356', '3876', '4107', '3878', '4127', '3879', '4303', '4282', '3490', '3931', '3491', '3509', '3482', '4285', '4202', '4367', '4302', '4307', '4338', '4350', '4311', '4280', '4274', '4294', '4312', '4200', '4295']
#print len(number_list)
#number_list += ['4264', '4265', '4069', '4256', '4230', '4337', '4085', '4050', '4213', '4239', '4253', '4198', '4277', '2773', '4027', '2749', '3511', '4214', '3887', '3858', '2759', '4222', '4270', '4248', '4354', '4271', '4290', '2767', '2750', '4098', '2753', '3964', '4130', '3898', '4148', '4078', '3912', '4122', '3483', '2756', '4076', '4173', '3501', '871', '901', '4049', '915', '4026', '4002', '1212', '2731', '2754', '2761', '4192', '2786', '3904', '2745', '2724', '3982', '890', '3957', '3953', '3940', '4007', '3890', '878', '3939', '2730', '3891', '4388', '4408', '2717', '104', '3978', '2737', '4001', '4381', '2711', '3990', '4009', '4335', '132']
for number in range(1,11):
    if number == 1:
        number = number_list[:8]
    else:
        number = number_list[number*8:(number+1)*8]
    a = threading.Thread(target=down,args=(number,))
    a.start()

