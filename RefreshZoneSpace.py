# encoding: utf-8
from http.cookiejar import MozillaCookieJar
from urllib.request import Request, build_opener, HTTPCookieProcessor
import urllib  
import re
import time
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"}
DEFAULT_TIMEOUT = 360
def grab(url):
    cookie = MozillaCookieJar()
    cookie.load('cookiesSpace.txt', ignore_discard=True, ignore_expires=True)
    req = Request(url, headers=DEFAULT_HEADERS)
    opener = build_opener(HTTPCookieProcessor(cookie))
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #print(response.read().decode('utf8'))
    urll=('https://user.qzone.qq.com/1334347212/main')
    req = Request(urll, headers=DEFAULT_HEADERS)
    opener = build_opener(HTTPCookieProcessor(cookie))
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #result=opener.open('https://h5.qzone.qq.com/mqzone/profile?starttime=1516453174071&hostuin=1334347212#1334347212/list/blog?res_uin=1334347212&starttime=1516453181975')
    html=response.read().decode('utf-8')
    #print(html)
    #html=result.read().decode('utf-8')
    #print(html)
    #pattern = re.compile(r'[\\u5e74\\u6708\\u65e5\d]+(?=\s*\\u4e4b\\u524d)') 
    itemContent=re.findall(r'try{return "(.*?)";} catch',html,re.I)
    print(itemContent)
    url='https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?g_tk=1158597849&qzonetoken='+str(itemContent[0])
    postdata2=urllib.parse.urlencode({
        'cgi':'http://taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6',
        'code':'502',
        'pathname':'/1334347212',
        'time':'-'+str(time.time()),
    }).encode(encoding='UTF8')
    timeNow=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    postdata=urllib.parse.urlencode({
        'code_version':'1',
        'con':'Hi! 现在时间是：'+timeNow+'，早上好！一日之计在于晨，早起的虫子被鸟吃，来点福利吧！复制此说说，打开最新版支付宝就能一起撸马云家的钱，一起分担马云日入亿元的烦恼，一起撸点早饭钱 rWAplq93vt 。',
        'feedversion':'1',
        'format':'fs',
        'hostuin':'1334347212',
        'paramstr':'1',
        'pic_template':'1',
        'qzreferrer':'https://user.qzone.qq.com/1334347212',
        'richtype':'',
        'richval':'',
        'special_url':'1334347212',
        'subrichtype':'',
        'syn_tweet_verson':'1',
        'to_sign':'0',
        'ugc_right':'1',
        'ver':'1',
    }).encode(encoding='UTF8')
    print(url)
    #req = Request('https://h5.qzone.qq.com/log/post/error/pc/emotion_cgi_publish_v6',data = postdata2, headers=DEFAULT_HEADERS)
    #response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #req = Request(str(url),data = postdata, headers=DEFAULT_HEADERS)
    #response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #req = Request(url, headers=DEFAULT_HEADERS)
    #opener = build_opener(HTTPCookieProcessor(cookie))
    #response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #for x in range(101):
      #items =html.find('qzonetoken')
      #print(html+str(x))
      #if items!=-1 :
#print(items)
          #break
    #jother='g_qzonetoken = (function(){ try{return (+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+[])+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(![]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+([]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+(![]+[])[!+[]+!![]]+([]+{})[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(!![]+[])[+[]]+([][[]]+[])[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]])())[+[]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+[])+(+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]]+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(![]+[])[+[]]+(+{}+[])[+!![]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(+{}+[])[+!![]]+(!+[]+!![]+[])+(!+[]+!![]+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[]);} catch(e) {var xhr = new XMLHttpRequest();xhr.withCredentials = true;xhr.open("post", "//h5.qzone.qq.com/log/post/error/qzonetoken\", true);xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");xhr.send(e);}})();'
    #ctx = execjs.compile('''function qzonetoken(){ location = 'http://user.qzone.qq.com/%s'; return %s}'''% ('1334347212',jother))
    #return ctx.call("qzonetoken")
    #ctx = execjs.compile('''function qzonetoken(){ location = 'http://user.qzone.qq.com/%s'; return %s}'''% ('1334347212','+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+[])+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(![]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+([]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+(![]+[])[!+[]+!![]]+([]+{})[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(!![]+[])[+[]]+([][[]]+[])[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]])())[+[]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+[])+(+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]]+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(![]+[])[+[]]+(+{}+[])[+!![]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(+{}+[])[+!![]]+(!+[]+!![]+[])+(!+[]+!![]+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[]'))
    #ctx = execjs.compile('''function qzonetoken(){return %s}'''% '')
	#return ctx.call('qzonetoken')
    #ctx = execjs.compile('''function qzonetoken(){ location = 'http://user.qzone.qq.com/%s'; return (+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+[])+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(![]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+([]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+(![]+[])[!+[]+!![]]+([]+{})[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(!![]+[])[+[]]+([][[]]+[])[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]])())[+[]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+[])+(+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]]+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(![]+[])[+[]]+(+{}+[])[+!![]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(+{}+[])[+!![]]+(!+[]+!![]+[])+(!+[]+!![]+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[]);}'''% ('133437212'))
    #ctx.call('qzonetoken',)
    #for i in ctx:
       #print(i)
if __name__ == '__main__':
  grab("https://h5.qzone.qq.com/mqzone/index?aid=549000929#info/all#addMood=true")