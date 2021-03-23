import urllib.request #21.2.26 不知道为毛有重复的
import re
import os
import time
def subject(url,File_name):
    if os.path.exists(File_name):
        os.removedirs(File_name)
    os.makedirs(File_name)
    url = url
    html = get_url(url)
    web_list = get_web_url(html)
    get_web(web_list,File_name)

def get_url(url):
    head={}
    head['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    req = urllib.request.Request(url,headers=head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
   # print(html)
    return html

def get_web_url(html):
    we_list = re.findall(r'href="https://(.*?\d\.(?:html))"',html)
    return we_list

def get_web(web_list,File_name):
    i = 0
    for ht in web_list:
        ht = "https://" + ht
        html = get_url(ht)
        DownLoad(html,File_name,i)
        i+=1

def DownLoad(html,File_name,i):
    img_list = re.findall(r'data-original="https://(.*?\.(?:jpg))',html)
    count = 0
    for tp in img_list:
        NaMe = str(i) + '-' + str(count) + '.' + tp.split(".")[-1]
        #print(NaMe)
        tp = 'https://' + tp
        urllib.request.urlretrieve(tp,File_name+'/'+NaMe)
        count +=1
        time.sleep(1)
if __name__ == "__main__":
    subject('https://www.cqjjkm.com/meizi','Zold2')#大F与煎蛋网的区分开


 