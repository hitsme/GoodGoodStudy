# encoding: utf-8
from http.cookiejar import MozillaCookieJar
from urllib.request import Request, build_opener, HTTPCookieProcessor
import urllib  
import re
import datetime
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
DEFAULT_TIMEOUT = 360
def grab(url):
    cookie = MozillaCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    req = Request(url, headers=DEFAULT_HEADERS)
    opener = build_opener(HTTPCookieProcessor(cookie))
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    print(response.read().decode('utf8'))
    result = opener.open('http://oa2.epoint.com.cn/EpointCommunity/EpointCommunity/Blog/BlogWrite.aspx')
    html = result.read()
    html=html.decode('utf-8')
    resu=html
    VIEWSTATE =re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', resu,re.I)
    EVENTVALIDATION =re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', resu,re.I)
    hidBelongUserGuid=re.findall(r'<input type="hidden" name="ctl00\$cphContent\$hidBelongUserGuid" id="ctl00_cphContent_hidBelongUserGuid" value="(.*)" />', resu,re.I)
    VIEWSTATEGENERATOR=re.findall(r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', resu,re.I)
    resultContent = opener.open('https://www.cnblogs.com/')
    htmlContent=resultContent.read().decode('utf-8');
    #print(htmlContent)
    itemContent=re.findall(r'<a class="titlelnk" href="(.*?)" target="_blank">(.*?)</a>',htmlContent,re.I)
    print(itemContent[0][0])
    comehereDay=datetime.datetime(2016,11,27)
    nowDay=datetime.datetime.now()
    haveDay=(nowDay-comehereDay).days
    print(haveDay)
    postdata=urllib.parse.urlencode({
        'UploadLib_Uploader_js':'1',
        '__EVENTARGUMENT':'',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':VIEWSTATE[0],
        '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR[0],
        '__EVENTVALIDATION':EVENTVALIDATION[0],
        'ctl00$Content$EpointHtmlEdit$FCKeditorHtmlEdit':'[EpointEndTag][EpointBeginTag]span style=\"font-weight: bold; font-size: 14pt;\"[EpointEndTag]日期标签（CH'+str(haveDay)+'）[EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style=\"font-family: 楷体,楷体_GB2312;\"[EpointEndTag][EpointBeginTag]span style=\"font-weight: bold; font-size: 14pt;\"[EpointEndTag]&nbsp; [EpointBeginTag]/span[EpointEndTag][EpointBeginTag]span style=\"font-size: 14pt;\"[EpointEndTag][EpointBeginTag]span style=\"font-size: 12pt;\"[EpointEndTag]'+itemContent[0][1]+itemContent[0][0]+'[EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style=\"font-family: 楷体,楷体_GB2312;\"[EpointEndTag][EpointBeginTag]span style="font-weight: bold; font-size: 14pt;\"[EpointEndTag]&nbsp; [EpointBeginTag]/span[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag]'+itemContent[1][1]+itemContent[1][0]+'[EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag][EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag][EpointBeginTag]p[EpointEndTag][EpointBeginTag]span style="font-family: 楷体,楷体_GB2312;"[EpointEndTag][EpointBeginTag]span style="font-size: 14pt;"[EpointEndTag][EpointBeginTag]span style="font-size: 12pt;"[EpointEndTag]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----由GoogleCloud强力驱动[EpointBeginTag]br[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/span[EpointEndTag][EpointBeginTag]/p[EpointEndTag]',
        'ctl00$Content$MySearchControl1$Ajax_search_Input_Text':'',
        'ctl00$Content$attach$Uploader1':'',
        'ctl00$Content$attach$txtFileDesc':'',
        'ctl00$Content$attach$uploadedFileCount':'0',
        'ctl00$Content$attach$uploadedTotalFileSize':'0',
        'ctl00$Content$btnAddNew':'发表主题',
        'ctl00$Content$ddlCategory':'0',
        'ctl00$Content$hidProjectGuid':'',
        'ctl00$Content$hidProjectName':'',
        'ctl00$Content$txtCategory':'如需新建请再此输入新的分类',
        'ctl00$Content$txtTag':'',
        'ctl00$Content$txtTitle':itemContent[0][1],
        'ctl00$ScriptManager1':'ctl00$Content$UpdatePanel2|ctl00$Content$btnAddNew',
    }).encode(encoding='UTF8')
    print(postdata)
    req = Request('http://oa2.epoint.com.cn/EpointCommunity/EpointCommunity/Blog/BlogWrite.aspx',data = postdata, headers=DEFAULT_HEADERS)
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #print(response.read().decode('utf8'))
	#return VIEWSTATE[0],EVENTVALIDATION[0]
    #print(html)
if __name__ == '__main__':
  grab("http://oa.epoint.com.cn")