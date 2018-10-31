# -*- coding:utf-8 -*-

"""
有道爬虫
"""

import urllib.request
import urllib.parse
import json


def youdao_translation(string):
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
    
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    
    target = json.loads(html)
    print("翻译结果:%s"%(target['translateResult'][0][0]['tgt']))

if __name__ == '__main__':
    content = '我爱你'
    youdao_translation(content)



