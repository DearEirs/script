#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2018-09-10 17:02:14


import sys
import time
import getopt
from multiprocessing import Process, cpu_count


def usage():
    doc = """
Usage: python cpu_test.py [options]
-c --cores <cores number>
           will consume number of cpu cores resources. default is all.
-t --time  <time>
           time script will run. defalut is 60s.
-h --help  get help.
example: python cpu_test.py  -c 10 -t 60
    """
    print(doc)
    sys.exit(0)


def compute(timeout):
    start_time = time.time()
    a = 0
    while 1:
        a = a + 1
        end_time = time.time()
        if end_time - start_time > timeout:
            break


def run(cpu_nums, timeout):
    processes = []
    for i in range(cpu_nums):
        p = Process(target=compute, args=(timeout,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   'hc:t:',
                                   ['help', 'time=', 'cores='])
    except getopt.GetoptError as e:
        print(e)
        usage()
    cpu_nums = cpu_count()
    timeout = 60
    for k, v in opts:
        if k in ('-h', '--help'):
            usage()
        elif k in ('-c', '--cores'):
            cpu_nums = int(v)
        elif k in ('-t', '--time'):
            timeout = int(v)
    print('start')
    run(cpu_nums, timeout)
    print('end')
