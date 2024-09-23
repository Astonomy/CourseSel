import requests
import urllib
from http import cookiejar
from PIL import Image,ImageFilter
import pytesseract
import json
from lxml import etree

login_url = 'https://sso.shisu.edu.cn/sso/login'
s = requests.session()
def get_dynamic(val):
    url = login_url
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    s.headers.update(headers)
    r = s.get(url=url,verify=False)
    dom = etree.HTML(r.content.decode('utf-8'))
    list = {}
    try: 
        result = dom.xpath(f'//input[@name="{val}"]')[0].get('value')
    except:
        print(val+' failed')
    return()


cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

login_url = 'https://sso.shisu.edu.cn/sso/login'
post_data = {}
post_data['lt'] = get_dynamic("lt")
post_data['execution'] = 'e1s1'
post_data['_eventId'] = 'submit'
post_data['authType'] = 'pwd'
post_data['isShowRandomCode'] = 0
post_data['un'] = input('username')
post_data['pd'] = input('passwd')
post_data['randomCode'] = ''

post_data = urllib.parse.urlencode(post_data).encode ('utf-8')

opener.open(login_url, post_data)
