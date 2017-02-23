# -*- encoding: utf-8 -*-

import requests
from lxml import  etree



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'origin':'https://www.google.com.hk',
    'referer':'https://www.google.com.hk/',
    'x-client-data':'CIu2yQEIo7bJAQjBtskBCIGZygEI+pzKAQipncoB',
    'cookie':'NID=96=bdVVALNWdNdW6O3Y0PSIekwsvxE6byLNYBcp-BkgYGYa1nNUI3xwWFkSZecgrS1bXOr-jwZytaQyHXOvxykuJbXUrdqAD9V_Itr8In2b_E70DObrxA4_4y2JHxQzv22S; UULE=a+cm9sZToxCnByb2R1Y2VyOjEyCnByb3ZlbmFuY2U6Ngp0aW1lc3RhbXA6MTQ4NjEwODY0NzQ0OTAwMApsYXRsbmd7CmxhdGl0dWRlX2U3OjIyMzk2NDI4MApsb25naXR1ZGVfZTc6MTE0MTA5NDk3MAp9CnJhZGl1czoxMjU1NTYyMA==',
}


def google_it(keyword):
    page_number = 0
    url = 'https://www.google.com.hk/search?safe=strict&site=&source=hp&q={0}&start={1}'.format(keyword,page_number*10)

    html = requests.get(url,headers=headers).text
    html = etree.HTML(html.lower())
    result = []
    for i in range(1,10):
        title = html.xpath(u'//div[@class="rc"][{0}]/h3/a/text()'.format(i))[0]
        link = html.xpath(u'//cite[{0}]/text()|//cite[{0}]/*/text()'.format(i))
        content = html.xpath(u'//span[@class="st"][{0}]/*/text()|//span[@class="st"][{0}]/text()'.format(i))
        link = ''.join(link)
        content = ''.join(content)
        result.append([title,link,content])
    return result
