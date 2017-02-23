#!/usr/bin/python
#coding: utf-8  
#Author:Dear
#检测服务器硬盘使用情况

import paramiko 
import threading
from smtplib import SMTP
from email.mime.text import MIMEText


def ssh2(ip,username,password,cmd):#ssh连接到服务器并执行命令
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip,22,username,password,timeout=5)
        except:
            ssh.connect(ip,2707,username,password,timeout=5)
        for i in cmd:
            input,output,error=ssh.exec_command(i)
            input.write('Y')
            out =output.readlines()
            file(out,ip)
        ssh.close()
    except:
        pass

def file(out,ip):#判断硬盘使用率是否超过95%
    for i in range(1,len(out)):
        b=out[i].split('%',1)[0][-3:]
        try:
            b=int(b.lstrip())
        except:
            b=0
        if b>95:
            email(ip)
            break

def email(ip):#发送邮件
    sender='sender@fnetlink.com'#发件人
    receiver='receiver@fnetlink.com'#收件人
    smtpserver='qq.smtp.com'#发件服务器
    password='your_password'
    msg=MIMEText('%s Hard drive has been used more than 95%s, please timely removal.'%(ip,'%'))#邮件内容
    msg['Subject']='Warning'
    msg['Form']='Your name'
    msg['To']="Receiver's name"
    smtp=SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.close()

if __name__=='__main__':
    cmd=['df -h']
    username="root"
    password="both-win"
    threads = []
    ip_list=['192.168.38.200','192.168.60.200','192.168.65.200','192.168.38.254']
    for ip in ip_list:
        t = threading.Thread(target=ssh2, args=(ip,username,password,cmd))
    for t in threads:
        t.join()

