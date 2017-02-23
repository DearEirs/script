#!/usr/bin/python
#coding: utf-8
#Author:Dear
#Date:2017-2-6

import paramiko

def ssh_conn(host,username,port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    password = raw_input('Please input your password:')
    ssh.connect(host, port, username, password, timeout=5)
    return ssh

def exec_comm(ssh_obj,mysql_user):
    mysql_password = raw_input("Please your mysql's password:")
    cmd = 'mysql -u{0} -p{1} -e {2}'.format(mysql_user,mysql_password,"'show databases'")
    input, output, error = ssh_obj.exec_command(cmd)
    out = output.readlines()
    ssh_obj.close()
    return out

if __name__ == '__main__':
    ssh_obj = ssh_conn(host='192.168.1.1',username='root')
    out = exec_comm(ssh_obj=ssh_obj,mysql_user='root')
    print out
