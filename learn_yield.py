#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-15 10:01:35

import time
import requests
from concurrent.futures import ThreadPoolExecutor


def blocking_func(url):
    html = requests.get(url)
    return html


def futures_gen():
    for url in urls:
        url = 'http://www.jianshu.com/p/' + url
        future = pool.submit(blocking_func, url)
        yield future


def coro_way():
    futures = []
    for future in futures_gen():
        futures.append(future)
    return [future.result() for future in futures]


def blocking_way():
    result = []
    for url in urls:
        url = 'http://www.jianshu.com/p/' + url
        html = requests.get(url)
        result.append(html)
    return result


def get_runtime(func):
    start = time.time()
    result = func()
    print(result)
    return time.time() - start


if __name__ == '__main__':
    urls = ['011b7d96f45e', '7b544e41a21b', '1de64126bfd5', '8c478fa04531']
    pool = ThreadPoolExecutor(20)
    print(get_runtime(coro_way))
    print(get_runtime(blocking_way))
