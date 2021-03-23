def b(arr):
    if len(arr)<2:
        return arr
    l=len(arr)-1 
    head=0
    key=arr[0]
    while head<l:
        while head<l and key<=arr[l]:
            l=l-1
        arr[head]=arr[l]
        while head<l and key>=arr[head]:
            head=head+1
        arr[l]=arr[head]
    arr[head]=key
    
    return b(arr[0:head]) + b(arr[head+1:])
arr=[3,4,7,0,2,8]
print(b(arr))
print(arr)
# 多出两步 当第一个为最小时 和就剩两个数并且不交换时 所以加两个if 失败版
#问题返回的数组无法替代原数组
#导致第2次引用后无效