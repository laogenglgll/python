'''有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数， 他说比第三个人大两岁,问第三个人，
又说比第二个人大两岁，问第二个人，又说比第1个人大两岁。 
最后问第一个人，他说是10岁。请问第5个人多大？
'''
@trace

def recursive_year(num):
    if num==1:
        a=input("请输入最后一个人的岁数")
        return a
    else:
        return int(2)+int(recursive_year(num-1))
num=int(input("要想第几个人的岁数"))
print(recursive_year(num))

