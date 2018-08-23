# encoding: utf-8
from http.cookiejar import MozillaCookieJar
from urllib.request import Request, build_opener, HTTPCookieProcessor
import urllib  
import re
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
DEFAULT_TIMEOUT = 360
def grab(url):
    cookie = MozillaCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    req = Request(url, headers=DEFAULT_HEADERS)
    opener = build_opener(HTTPCookieProcessor(cookie))
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    print(response.read().decode('utf8'))
    result = opener.open('http://oa.epoint.com.cn')
    html = result.read()
    html=html.decode('utf-8')
    print(html)
    result = opener.open('http://oa.epoint.com.cn/netoffice8/ZReport/Pages/Problem/Problem_Add.aspx')
    html = result.read()
    html=html.decode('utf-8')
    resu=html
    #print(resu)
    result = opener.open('http://oa2.epoint.com.cn/EpointCommunity/EpointCommunity/Home/Home.aspx')
    html = result.read()
    html=html.decode('utf-8')
    resu=html
    #print(resu)
if __name__ == '__main__':
  grab("http://oa.epoint.com.cn")