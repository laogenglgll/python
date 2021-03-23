#汉诺塔游戏
def recursive_num(n,x,y,z):
    global num
    if n==1:
        print(x,"->",z)
        num+=1
    else:
        recursive_num(n-1,x,z,y)
        print(x,"->",z)
        num+=1
        recursive_num(n-1,y,z,x)
n=int(input("输入安诺塔层数:"))
num=0
recursive_num(n,'x','y','z')
print(num)
