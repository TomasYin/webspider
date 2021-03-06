# !/urs/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import os
import random

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    
    proxies = ['61.135.217.7:80','218.14.115.211:3128','122.114.31.177:808','121.196.218.197:3128','14.118.252.59:6666','106.56.102.163:8070','222.171.83.213:63000','14.118.252.202:6666']
    proxy = random.choice(proxies)
    
    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    
    
    response = opener.open(req)
    html = response.read().decode('utf-8')
    html = response.read()
    return html
    
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addr = []
    
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addr.append(html[a+9,b+4])
        else:
            b = a + 9
        a = html.find('img src=',b)
    
    return img_addr
    

def save_imgs(img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))
    
    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()
        
    
