a=[1,2,3,4,5,6]
b=0
while b<len(a):
    print(a)
    b+=1
'''    这个比上边少一部判断
alist = range(5)
it = iter(alist)

while True:
    try:
        print(next(it))
    except StopIteration:
        break'''