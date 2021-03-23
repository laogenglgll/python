x=7
i=1
ladder=0
while ladder==0 and i<100 :
    if x%2==1 and x%3==2 and x%5==4 and x%6==5:
        ladder=1
    else:
        x=7*(i+1)
        i=i+1
if ladder==1:
    print(x)
else:
    print("范围内无答案！")