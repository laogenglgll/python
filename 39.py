import urllib.request
import time
url = 'https://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'https':'67.172.180.46:33428'})
opener = urllib.request.build_opener(proxy_support)
opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36Edge/13.10586')]
opener.open(url)
request = urllib.request.urlopen(url)
html = request.read().decode('utf-8')
print(html)