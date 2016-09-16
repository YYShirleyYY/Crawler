# -*- coding: UTF-8 -*-

import urllib
import urllib2
import requests
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    response=requests.get(url,headers=headers)
#    request = urllib2.Request(url,headers=headers)
#    response = urllib2.urlopen(request)
    content = response.text
    
    pattern_t = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>',re.S)
    items = re.findall(pattern_t,content)
    for item in items:              
        print 'author: ',item[0]       
        str_item=item[1].encode('utf-8')
        p=re.compile('<br/>')
        str_item2=p.sub('\n',str_item)
               
        print str_item2   
        
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason 
