#!/usr/bin/python3.5
import sys
from html.parser import HTMLParser

import requests

#使用HTMLParser解析html，默认从头解析到尾，如果在其中置一个标志位，则可以实现只在某段html解析中，使用handle_data()
class myParser(HTMLParser):
    a_text = False
    distance = ''
    def handle_starttag(self,tag,attrs):
        if tag=="h3":
            self.a_text=True    #遇到h3开始的标签，置标志位
    def handle_endtag(self,tag):
        if tag=="h3":
            self.a_text=False   #遇到h3结束的标签，取消标志位
    def handle_data(self,data):
        if self.a_text is True: #如果置标志位，则输出
            #print(data)
            self.distance = data
    def get_distance(self):
        return self.distance

data={
    'shikechaxun':'时刻查询',
    'txtChufa':sys.argv[1],
    'txtDaoda':sys.argv[2],
}
s = requests.session()
raw = s.get('http://juli.liecheshike.com/juli/',data=data)
result = raw.text
query = myParser()
# print(result) #result是整个html
query.feed(result)
distance = query.get_distance()
print(distance)
query.close()


