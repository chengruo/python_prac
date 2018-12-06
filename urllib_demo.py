import urllib
from urllib import request
from urllib import error
from urllib import parse
from urllib import robotparser
import http.cookiejar
import requests

#response = urllib.request.urlopen('http://www.baidu.com')

#cookie = http.cookiejar.CookieJar()
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#response = opener.open('http://www.weibo.com')
#for item in cookie:
#    print(item.name'='item.value)

#r = requests.get('https://api.github.com/events')
#r = requests.post('http://httpbin.org/post', data = {'key':'value'})

#url = 'http://10.50.13.102:9991'
url = 'http://172.19.135.12:9991'
#Guid&TVGuid为  code2
#select MamId from AssetIdMap where AssetType='0' and Asset_Id='7c908e50e22211e295bbd1de78467b5d' and SPCode='CIP'
m1 = {'request':'' ,
     'flvpath':'77088013145205e5b90232bec0000112_h2641300000mp296.ts',
      'flvpath':'77088013145205c5b90232bec0000001_h2642200000mp296.ts',
      'Video_title_codeF':'77088013145205c5b90232bec0000001',
      'Video_title_codeB':'h2642200000mp296.ts',
        'f_pgmname':'蓝精灵123',
       'f_pgmtime':'2017-08-02 23:48:24',
      'pglength':'',
      'Fpc':'CCTV',
      'f_pgmtitle':'','f_pgmbrief':'',
      'Reserv1':'','Reserv2':'wxsb01',
      'Reserv3':'tanglong','Reserv4':'2017-02-22 23:48:00',
      'Reserv5':'','Reserv6':'',
      'Reserv7':'','Reserv8':'','Edit_mode':'1',
      'Video_part':'0',
      'Video_part_time':'300',
      'wmvpath':'','pgmbw':'',
      'imgpath1':'','imgpath2':'','imgpath3':'','columnname':'',
      'Fpt':'2017-01-21 23:47:47'
}

m2 = {  'Protocoltype':'1',
        'Guid':'00000102000000010000000039771752',
         'TVGuid':'00000102000000010000000039771752',
         'Title':'nihao',
         'DescriptionofContent':'nihao',
         'Rtime':'2021-02-10 23:00:00',
        'ContentProvider':'CIP',
        'ShowDate':'2017-02-10 23:00:00',
        'Duration':'34534',
        'SeqNo':'24',
        'Class':'kath',
        'Kpeople':'是不是中国人啊·jekwfhweff,dwquhdweh',
        'Director':'wefewjf',
        'Producer':'tanglong',
        'Cataloger':'zhangjia',
        'PgmCategory':'zhangjia',
        'PgmSndClass':'zhangjia',
        'Keyword':'zhangjia',
        'Dsc':'python',
        'Source':'wxsb01',
        }


r = requests.post(url,m2)
print(r)
