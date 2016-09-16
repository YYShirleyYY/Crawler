# -*- coding: UTF-8 -*-
import requests
import re
import pickle
import json
import sys

from bs4 import BeautifulSoup

saveout=sys.stdout
fsock=open('out.html','w')
sys.stdout=fsock
# url地址
url = 'http://202.119.4.150/nstudent/'
login_url = url+'/login/aspx'

# 表单数据
login_data = {
    '__VIEWSTATE': 'dDw2Nzg5Mjk2NTY7O2w8b2s7Pj48MknpZN4t3xVYoaVlFnNMsdAYgA==',
    'ok.x': '28',
    'ok.y': '11',
    'txt_password': '',
    'txt_user': '',
    
}

user_agent ='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
accept_encoding='gzip, deflate'
connection='keep-alive'
content_type='application/x-www-form-urlencoded'
header= { 'User-Agent' : user_agent,'Accept-Encoding':accept_encoding,'Connection':connection,'Content-Type':content_type,}


# 使用requests模拟浏览器发起post请求
s = requests.session()
s.post(login_url,headers=header,data=login_data)
r=s.get(url)
# 居然是用GB2312编码的
#print r.text.encode('GB2312')
print r.content
# 浏览器也会返回cookie数据

sys.stdout=saveout
fsock.close()
print s.cookies

