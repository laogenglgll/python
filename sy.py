url='http://ip.webmasterhome.cn/'

proxy_support=urllib.request.ProxyHandler({'http':'110.73.47.45:8123'})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('gb2312')
print(html)