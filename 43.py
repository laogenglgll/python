#煎蛋网2020年的爬虫网上找的
from urllib import request
import os #创建打开读写文件的模块-
import re #引入正则表达式模块
from urllib.request import urlretrieve
#import Requests
 
 
def get_picaddress(html,fold,i):
    img_list = re.findall(r'src="(//.*?\.((?:jpg|png))"',html)#\. 把点当作普通字符匹配   (?:后面匹配的不输出)
    #http://wx1.sinaimg.cn/mw600/0076BSS5ly1gnznuv68nbj30u0193jw7.jpg
    count = 0
    for ad in img_list:
#        print(ad)
        address = "http:"+ad
#        print(address)
        picname = str(i)+"_"+str(count)+"."+address.split(".")[-1]
#        print(picname)
        urlretrieve(address,fold+"/"+picname)#urlretrieve把网上数据保存到本地
        count+=1
        
def get_html(url):
    headers ={}
    headers["User-Agent"]="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    res = request.Request(url,headers=headers)
    response = request.urlopen(res)
    html = response.read().decode("utf-8")
#   print(html)
    return html
    
def downloadpic(fold="picfold",page=10):
    if os.path.exists(fold):
        os.removedirs(fold)
    os.makedirs(fold,exist_ok=True)
    url = "http://jandan.net/ooxx"
    regex = re.compile(r'href="(.*?)" class="previous-comment-page"')#在网页中查找符合的数据
    print(regex)
    for i in range(10):
        if i ==0:
            pass
        else: 
            html = get_html(url)
            preurl = regex.findall(html)[0]
            print(preurl)
            url = "http:"+preurl
        html = get_html(url)
        get_picaddress(html,fold,i)
              
if __name__ == "__main__":
    downloadpic()