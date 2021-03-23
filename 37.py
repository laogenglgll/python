import urllib.request
import urllib.parse
import json
import time
while True:
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com"
    data = {}
    data['i']='你妹的'
    data['type']= 'AUTO'
    #data['to']= 'AUTO'
    #data['smartresult']= 'dict'
    #data['client']:='fanyideskweb'   戴上它就出错是子脚本 不知道什么龟毛病

    data['doctype'] ='json'
    data['version'] ='2.1'#版本 win默认可有可无
    data['keyfrom'] ='fanyi.web'
    data['ue'] = 'UTF-8'#使用什么方式转换 win默认的是utf-8 可有可无
    data['typoResult'] = 'true'
    #data['action']= 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')
    #第一种自前面添加head  在urlopen种添加一个head
    head={}
    #head['Referer'] = 'http://fanyi.youdao.com/'
    head['user-Agrnt']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    #response = urllib.request.urlopen(url,data,head)
    req = urllib.request.Request(url, data) #不加head可以直接打开网页直接写下一步但是加护dead需要request
    #分两步 
    #第二种 req.add_header('user-Agrnt','illa/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36 Edg/88.0.705.74')
    print(type(req))
    response = urllib.request.urlopen(req)
    print(type(response))
    html = response.read().decode('utf-8')
    print(type(html))
    print(html)
    html = json.loads(html)#json 一种轻量级的数据交换格式 方便服务器数据交换需要使用函数转换为字典
    print(html)
    print(html['translateResult'][0][0]['tgt'])
    #EOL while scanning string literal错误大概是 ' 符号不对
    #有两种方法隐藏自己
    time.sleep(2)#防止单位时间内访问太多被拒绝 延迟访问    （ip地址）

