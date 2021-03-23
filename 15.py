#数列相加
arr=list(input().split(" "))
def sum (brr):
    if len(brr)==0: # 或者brrr[]   因为空的列表为假
        return 0
    else:
        return int(brr[0]) +int(sum(brr[1:]))
        
# 奶奶个腿的 + 号两侧雷类型相同  

print(sum(arr))