#导入requests包
import requests  

#进行UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

#指定url
url = 'https://m10.music.126.net/20200715163315/a075d787d191f6729a517527d6064f59/ymusic/0552/0f0e/530f/28d03e94478dcc3e0479de4b61d224e9.mp3'

#调用requests.get方法对url进行访问，和持久化存储数据
audio_content = requests.get(url=url,headers=headers).content

#存入本地
with open('空山新雨后.mp3','wb') as f :
    f.write(audio_content)

print("空山新雨后爬取成功！！！")