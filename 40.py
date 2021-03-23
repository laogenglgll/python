import urllib.request
def ip():
    try:
        url = 'https://www.whatismyip.com.tw/'
        proxy_support = urllib.request.ProxyHandler({'http':'47.94.145.95:81'})
        # 接着创建一个包含代理IP的opener
        opener = urllib.request.build_opener(proxy_support)
        # 安装进默认环境
        urllib.request.install_opener(opener)
        # 试试看IP地址改了没
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        print(html)
    except:
        ip()
ip()