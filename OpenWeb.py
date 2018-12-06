#import urllib.request
#url = 'https://www.zhihu.com/signin?next=%2Fquestion%2F42123344'
#response = urllib.request.urlopen(url)
#code = response.getcode()
#html = response.read()
#mystr = html.decode("utf8")
#response.close()
#print(mystr)

import requests
r = requests.get("https://api.github.com/events")
print(r.text)