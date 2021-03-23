#变量之间要有，号  直接打印或者转移的要用“或者‘号括起来
print("red\tyellow\tgreen")
for red in range(4):
    for yellow in range(4):
        for green in range(2,7):
            if red+yellow+green==8:
                print(red,'\t',yellow,'\t',green)