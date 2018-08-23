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
    result = opener.open('http://oa.epoint.com.cn/netoffice8/ZReport/Pages/Problem/Problem_Add.aspx')
    html = result.read()
    html=html.decode('utf-8')
    resu=html
    VIEWSTATE =re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', resu,re.I)
    EVENTVALIDATION =re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', resu,re.I)
    hidBelongUserGuid=re.findall(r'<input type="hidden" name="ctl00\$cphContent\$hidBelongUserGuid" id="ctl00_cphContent_hidBelongUserGuid" value="(.*)" />', resu,re.I)
    VIEWSTATEGENERATOR=re.findall(r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', resu,re.I)
    print(VIEWSTATEGENERATOR)
    postdata=urllib.parse.urlencode({  
        'ctl00$ScriptManager1':'ctl00$UpdatePanel1|ctl00$cphToolBar$submit',
        'UploadLib_Uploader_js':'1',
        'ctl00_cphContent_Tab1_ClientState':'{\"ActiveTabIndex\":0,\"TabState\":[true,true]}',
        'ctl00_cphContent_Tab1_DataGrid1_ClientState':'{}',
        'ctl00_cphContent_Tab1_DataGrid2_ClientState':'{}',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':VIEWSTATE[0],
        '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR[0],
        '__EVENTVALIDATION':EVENTVALIDATION[0],
        'ctl00$cphContent$IsNoProblem':'on',
        'ctl00$cphContent$textarea':'',
        'ctl00$cphContent$CuteWebUIUpload1$Uploader1':'',
        'ctl00$cphContent$CuteWebUIUpload1$uploadedTotalFileSize':'',
        'ctl00$cphContent$CuteWebUIUpload1$uploadedFileCount':'',
        'ctl00$cphContent$CuteWebUIUpload1$Attachments1':'',
        'ctl00$cphContent$CuteWebUIUpload1$hidGuidLst':'',
        'ctl00$cphContent$CuteWebUIUpload1$hidFileNameLst':'',
        'ctl00$cphContent$CuteWebUIUpload1$HidAttachGuid':'',
        'ctl00$cphContent$hidChangeType':'',
        'ctl00$cphContent$hidChangeValue':'',
        'ctl00$cphContent$HidDelGuid':'',
        'ctl00$cphContent$hidBelongUserGuid':hidBelongUserGuid[0],
        'ctl00$cphContent$ProblemGuid':'',
        'ctl00$cphContent$date':'',
        '__ASYNCPOST':'true',
        'ctl00$cphToolBar$submit':'提交'
    }).encode(encoding='UTF8')
    print(postdata)
    req = Request('http://oa.epoint.com.cn/netoffice8/ZReport/Pages/Problem/Problem_Add.aspx',data = postdata, headers=DEFAULT_HEADERS)
    response = opener.open(req, timeout=DEFAULT_TIMEOUT)
    #print(response.read().decode('utf8'))
	#return VIEWSTATE[0],EVENTVALIDATION[0]
    #print(html)
if __name__ == '__main__':
  grab("http://oa.epoint.com.cn")