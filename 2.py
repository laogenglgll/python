#if和else要严格使用缩进 否则会出错
#input() 必须带括号 可以里面没东西 输入的是 str 类型 与int类型比较要用int()强制转换
import random
times=3
secret=random.randint(1,10)
print(".........欢迎老耿来到python.........")
gess=int(input("打一个数字吧"))

while(gess!=secret and times!=0):

    times=times-1
    if gess>secret :
        print("你猜大了")
    else :
        print("你猜小了")
    print("你猜错了")
    print("再猜一次吧")
    print("输入一个数吧！")
    gess=int(input())
print("恭喜你猜对了")
print("游戏结束")