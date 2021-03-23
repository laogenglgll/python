#只能同类型相加+例如str+str  判断是否是整数还有如下方式 else+if=elif
temp=input("请输入年份")
while not temp.isdigit():
    temp=input("抱歉你输入的不是年份，请重新输入")
year=int(temp)
if year/400==int(year/400):
    print(temp+"是闰年")
elif year/4==int(year/4) and year/100!=int(year/100):
    print(temp+"是闰年！")
else:
    print(temp+"不是闰年！")
