# -*- coding: UTF-8 -*-

#http://liam0205.me/2016/02/27/The-requests-library-in-Python/
import requests
import re
import sys

saveout=sys.stdout
fsock=open('github.html','w')
sys.stdout=fsock

url1   = 'https://github.com/login'
url2   = 'https://github.com/session'
user = ''
password=''
my_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Accept-Encoding' : 'gzip',
    }
s=requests.Session()
r=s.get(url1,headers=my_headers)
print r.content
#浏览器对标签属性解析的顺序会不同，要注意正则表达式。
reg='<input name="authenticity_token" type="hidden" value="(.*)" />'
pattern=re.compile(reg)
result=pattern.findall(r.content)
sys.stdout=saveout
fsock.close()
print result


my_data={
    'authenticity_token':result,
    'commit':'Sign in',
    'login':user,
    'password':password,
    'utf8':'%E2%9C%93'
    }

r2 = s.post(url2,headers=my_headers, data = my_data)
print r2.url, r2.status_code, r2.history
