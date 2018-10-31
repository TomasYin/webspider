# -*- coding:utf-8 -*-

"""
有道爬虫(修改)
"""

import urllib.request
import urllib.parse
import json


def youdao_translation_new(string):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data['i'] = string
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1528785348581'
    data['sign'] = '34d41730de218d4bd84f2b9c6c6ff28d'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    
    data = urllib.parse.urlencode(data).encode('utf-8')
    
    # 方法一,提前在urllib.request.Request中加上head：
    #head = {}
    #head['User-Agent'] = 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    #req = urllib.request.Request(url,data,head)
    
    # 方法二,使用add_header加上head:
    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    
    target = json.loads(html)
    print("翻译结果:%s"%(target['translateResult'][0][0]['tgt']))

if __name__ == '__main__':
    content = input("请输入你想翻译的内容：")
    youdao_translation_new(content)



