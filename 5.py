#for循环里i的变化并不会改变接下来循环i的值  会从range中取下一个i的值
for i in range(10):
    if i%2!=0:
        print(i)
        continue
    else:

        i+=2
        print(i)