#网易云爬取单个音乐     
import requests

head={}
head['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

url = "https://m801.music.126.net/20210302130624/65382bff36896acf351d7eeb0f3d5b87/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/5640428920/e99c/9015/2057/d7fa4163b75631c062223dbe42b76218.m4a"

req = requests.get(url,headers=head).content
with open('歌名1.m4a','wb') as f:
    f.write(req)
print("歌名下载成功")
