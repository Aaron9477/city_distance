#!/usr/bin/python3.4
import sys
from html.parser import HTMLParser

import requests


class myParser(HTMLParser):
    a_text=False
    def handle_starttag(self,tag,attrs):
        if tag=="h3": #只有结果的标签是h3
            self.a_text=True
    def handle_endtag(self,tag):
        if tag=="h3":
            self.a_text=False
    def handle_data(self,data):
        if self.a_text is True:
            print(data)

data={
    'shikechaxun':'时刻查询',
    'txtChufa':sys.argv[1],
    'txtDaoda':sys.argv[2],
}
s=requests.session()
raw=s.get('http://juli.liecheshike.com/juli/',data=data)
result=raw.text
query=myParser()
query.feed(result)
query.close()
