list1 = ['1.Jost do It','2.一切皆有可能','3.让变成改变世界','4.Impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]#[2:把数字和点去掉]    两个for循环


print(list3)
for each in list3:
    print(each)