#!/bin/env/
# -*- coding:utf-8 -*-

import requests
import re
import json
"""
1.获取影响ID,获取JS的URL地址源码 “https://lol.qq.com/biz/hero/champion.js”
2.拼接URL地址:http://ossweb-img.qq.com/images/lol/web201310/skin/big英雄的ID皮肤的序列.jpg
3.获取下载图片的名称
4.下载图片

"""

def getLOLImages():
    dict_js = getJS_URL()
    url_list = joint_URl(dict_js)
    list_filepath = get_PicName(dict_js)
    download_Pic(url_list,list_filepath)
    
def getJS_URL():
    # 获取JS URL地址源代码 
    url_js = "https://lol.qq.com/biz/hero/champion.js"
    html_js = requests.get(url_js).text
    # 200状态码  访问成功
    #print(html_js)
    
    # 正则表达式 .*?,"data"
    reg = '"keys":(.*?),"data"'
    list_js = re.findall(reg,html_js)
    #print(type(list_js[0]))
    
    # 从str装换到dic类型
    dict_js = json.loads(list_js[0])
    #print(type(dict_js))
    #print(dict_js['266'])
    #print(dict_js)
    return dict_js

def joint_URl(dict_js):
    # 拼接URl地址
    url_list = []
    for key in dict_js.keys():
        # 英雄的ID
        #print(key,value)
        
        for i in range(20):
            i = str(i)
            if len(i) == 1:
                hero_num = "00" + i
            elif len(i) == 2:
                hero_num == '00'
        num_str = key + hero_num
        
        url = "http://ossweb-img.qq.com/images/lol/web201310/skin/big" + num_str +'.jpg'
        #print(url)
        url_list.append(url)
    #print(url_list)
    return url_list

def get_PicName(dict_js):
    # 获取下载图片的名称
    list_filepath = []
    path = r"G:\mygit\webspider\LOLPic\\"
    for name in dict_js.values():
        #print(name)
        for i in range(20):
            file_path = path + name +str(i) + '.jpg'
            #print(file_path)
            list_filepath.append(file_path)
    return list_filepath
    
def download_Pic(url_list,list_filepath):
    # 下载图片
    n = 0
    for picurl in url_list:
        #print(picurl)
        res = requests.get(picurl)
        n += 1
        # 通过判断状态码来去掉多余的空白皮肤
        if res.status_code == 200:
            print("正在下载%s"%list_filepath[n])
            # w write b 二进制数据格式
            with open(list_filepath[n],'wb') as f:
                # 获得网页内容
                f.write(res.content)
        
if __name__ == '__main__':
    getLOLImages()