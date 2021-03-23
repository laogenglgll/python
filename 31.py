#Myproperty实际是一个类有着调用x的方法但是通过这个一个类调用
#另一个类实现对进来的值的改变在放回复制给x
#raise stopiteration是什么意思  raise 用来引发异常 后面的语句
# 不执行
'''__ len__(self)	定义当被len()函数调用时的行为（返回容器中元素的个数）
__ getitem__(self, value)	定义获取容器中指定元素的行为，相当于self[key]
__ setitem__(self, key, value)	定义设置容器中指定元素的行为，相当于self[key]=value
__ delitem__(self, key)	定义删除容器中指定元素的行为，相当于del self[key]
__ iter__(self)	定义当迭代容器中的元素的行为
__ reversed__(self)	定义当被reversed()函数调用时的行为
__ contains__(self, item)	定义当使用成员测试运算符（in或not in）时的行为

作者：无罪的坏人
链接：https://www.jianshu.com/p/de802127eb62
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
>>> class CountList:
    def __init__(self, *args):  # 可变数量的参数
        self.values = [x for x in args]  # 把参数转换成列表
        self.count = { }.fromkeys(range(len(self.values)), 0)  # 给字典初始化
        # 这里是有列表的下表作为字典的键，注意不能用元素作为字典的键
        # 因为列表的不同下标可能有值一样的元素，但字典不能有两个相同的键
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):#getitem 是字典相加是调用

        self.count[key] += 1
        return self.values[key]

    
>>> c1 = CountList(1, 3, 5, 7, 9)
>>> c2 = CountList(2, 4, 6, 8, 10)
>>> c1[1]
3
>>> c2[1]
4
>>> c1[1] + c2[2]
9
>>> c1.count
{0: 0, 1: 2, 2: 0, 3: 0, 4: 0}
>>> c2.count
{0: 0, 1: 1, 2: 1, 3: 0, 4: 0}