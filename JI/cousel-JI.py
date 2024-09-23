import requests
import urllib
from http import cookiejar
from PIL import Image,ImageFilter
import pytesseract
from lxml import etree
import json
import re

cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

login_url='https://jaccount.sjtu.edu.cn/jaccount/ulogin'
url =  'https://jaccount.sjtu.edu.cn/jaccount'

def re_search(retext, text):
    tmp = re.search(retext, text)
    if tmp:
        return tmp.group(1)
    else:
        return None

session = requests.Session()
def _get_login_page(session, url):
    # return page text
    req = session.get(url)
    # if last login exists, it will go to error page. so ignore it
    if '<div id="login-form">' in req.text:
        return req.text
    else:
        print('get fail')

req = _get_login_page(session, url)

post_data = {}
post_data['sid'] = 'jaoauth220160718'
post_data['client'] = re_search(r'client: "(.*?)"', req)
'''
post_data['returl'] = get_dynamic('returl')
post_data['se'] = get_dynamic('se')
post_data['v'] = ''
post_data['uuid'] = get_dynamic('uuid')
post_data['user'] = input('username')
post_data['pass'] = input('passwd')
post_data['captcha'] = captachaCode
post_data['lt'] = 'p'

post_data = urllib.parse.urlencode(post_data).encode ('utf-8')

opener.open(login_url, post_data)
'''
print(post_data)
