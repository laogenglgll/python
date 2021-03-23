def quick_sort(data):
    """quick_sort"""
    if len(data) >= 2:#判断长度
        mid = data[len(data)//2]#取中间的
        left,right = [], []
        data.remove(mid)#移除列表中某个项
        for num in data:
            if num >= mid: # 分为两个列表 一个比mid 大 一个mid小#等于左边比mid小右边比mid大
                right.append(num)#结尾加个元素
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data