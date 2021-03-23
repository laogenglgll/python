import re
a=[1,2,3,4]
a[3]='nimei'
a[1]='nima'
a[2]='nidie,niam,nidie'
print(a[2])
print(re.findall(r"ni",a[2]))