import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()
with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_img)

req = urllib.request.Request("http://placekitten.com/g/200/400")
response2 = urllib.request.urlopen(req)
cat_img2 = response2.read()
with open('cat_200_400.jpg', 'wb') as f:
    f.write(cat_img2)
print("nimei")