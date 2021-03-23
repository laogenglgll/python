import urllib.request #煎蛋网爬虫照着43写的
import re
import os
import time

def subject(num,File_name):
    url = "http://jandan.net/ooxx"
    if os.path.exists(File_name):
        os.removedirs(File_name)
    os.makedirs(File_name)
    for i in range(num):
        if i == 0:
            pass
        else:
            html = get_url(url)
            url1 = re.findall(r'href="(.*?)" class="previous-comment-page"',html)
            #print(url)
            url=url1[0]
            url = 'http:'+url
        html = get_url(url)
        DownLoad(html,File_name,i)

def get_url(url):
    head = {}
    head['user-agent'] = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    res = urllib.request.Request(url,headers=head)
    response = urllib.request.urlopen(res)
    html = response.read().decode('utf-8')
    #print(html)
    return html

def DownLoad(html,fold,i):
    img_list = re.findall(r'src="(//.*?\.(?:jpg|png))"',html)
    count = 0
    for ht in img_list:
        img_name = str(i) + '_' +str(count) + '.' + ht.split(".")[-1]
        ht = "http:" + ht 
        #print(ht)
        urllib.request.urlretrieve(ht,fold+"/"+img_name)
        count +=1
        time.sleep(1)
if __name__ == "__main__":
    
    subject(10,'fold2')
