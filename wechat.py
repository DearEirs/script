# -*- encoding: utf-8 -*-
import itchat
from itchat.content import *
import weather
from google_spider import google_it
from urllib2 import quote
import  time
'''
@itchat.msg_register(TEXT,isFriendChat=True)
def send_to_myself(msg):
    if msg['Type'] == TEXT and 'Dear' in msg['FromUserName']  :
        return  'hello Dear'
 '''

itchat.auto_login(hotReload=True)

a = u'@我替做咩'
b = u'小矮人'

@itchat.msg_register(TEXT, isGroupChat = True)
def group_reply(msg):
    if msg['isAt'] == True :
        print(1)
        itchat.send ('%s %s' % (a,msg['ActualNickName']),toUserName=b)
        print(msg['ActualNickName'])
        print(msg['MsgType'],msg['AppMsgType'])
        print('text')

name = u'咸湿'
wea = u'天气'

'''
@itchat.msg_register(TEXT)
def one_to_one(msg):
    print(msg['Text'])
    print(msg)
    if msg['Text']== name:
        itchat.send_image(r'D:/x1.jpg', toUserName=msg['FromUserName'])
        return None
    elif msg['Text']== wea:
        w = weather.start()
        result = ""
        for i in w:
            result = result + i + '\n'
        itchat.send(msg=result,toUserName=msg['FromUserName'])
        return None
    else:
        return None
    return 'You said to me one to one: %s' % msg['Text']
'''

@itchat.msg_register(TEXT)
def one_to_one(msg):
    if msg['Text']:
        key = msg['Text'].encode('utf8')
        key = quote(key)
        data = google_it(key)
        for i in data:
            text = "%s%s%s" % (i[0],i[1],i[2])
            itchat.send(msg=text,toUserName=msg['FromUserName'])
            time.sleep(1)
    return None

itchat.run()