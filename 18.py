def quicksort(a, left, right):
    if left>=right:
        return -1
    temp=a[left]
    i=left
    j=right
    while i!=j:
        while a[j]>=temp and i<j:
            j-=1
        while a[i]<=temp and i<j:
            i+=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[left]=a[i]
    a[i]=temp    
    quicksort(a,left,i-1)
    quicksort(a,i+1,right)


a=[8,4,7,0,3,9]
quicksort(a,0,len(a)-1)
print(a)
