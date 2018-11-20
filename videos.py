# -*- coding:utf-8 -*-

import requests
from lxml import etree

class Video_Spader(object):
    def start_request(self):
        # 通过网页的url获得整体数据
        response = requests.get("https://ibaotu.com/shipin/")
        #print(response.text)
        # 抽取想要的视频数据 src视频连接
        text = response.text
        self.xpath_data(text)
    
    def xpath_data(self,text):
        html = etree.HTML(text)
        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        video_title = html.xpath('//span[@class="video-title"]/text()')
        #print(video_src,video_title)
        self.with_file(video_src,video_title)
    
    def with_file(self,video_src,video_title):
        # 匹配视频的src和title
        for src,title in zip(video_src,video_title):
            #print(src,title)
            response = requests.get("https:"+src)
            filename = title + ".mp4"
            print("正在爬取%s"%filename)
            path_file = "G:\mygit\webspider\Video_Spider\\" + filename
            with open(path_file,'wb') as f:
                f.write(response.content)

if __name__ == "__main__":
    spider = Video_Spader()
    spider.start_request()
    
    

