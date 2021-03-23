	# 正常人的
	 def transpose(arr):
		result, arr_len = list(), len(arr)
		for j in range(len(arr[0])):
			result.append(list())
			for i in range(arr_len):
				result[-1].append(arr[i][j])
	return result

print(transpose([[1,2,3], [4,5,6], [7,8,9]]))
#列表推导式 可读性下降
>>> def transpose(arr):
		rerurn [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]

>>> transpose([[1,2,3], [4,5,6], [7,8,9]])
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#lambda函数的用法 :后无表明返回值默认为lambda 后边的x
#[x for x in range(1,100)if x%3==0] ⬅下边三个的列表推导式表达方法
a = list(filter(lambda x:x%3 == 0,range(1,100)))
print(a)

b = list(filter(lambda x:not(x%3),range(1,100)))
print(b)

c = list(filter(lambda x:x if x%3==0 else None,range(100)))
print(c)
#zip（）函数用法
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)] 
>>> a1, a2 = zip(*zip(a,b))   # (感觉没啥比用)与 zip 相反，*zip 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>>
#函数递归例子
#常规写法：

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i

    return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))
#递归写法：

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))
#汉诺塔
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        hanoi(n-1,x,z,y)#将x上的前n-1个盘移动到y上
        print(x,'->',z)#将x上的n盘移动到z上
        hanoi(n-1,y,x,z)#将y盘上的n-1个盘移动到z上

n = int(input('请输入汉诺塔的层数：'))
hanoi(n,'X','Y','Z')
#10进制转2进制   8除以2除到底的过程
def binB(num):
    # 剥洋葱思路
    # 每一次都要做两件事 num // 2; num % 2
    # 先预设一个空字符串: result
    result = ''

    if num:
        # 开始剥洋葱 num // 2，直到洋葱皮剥完为止
        # 当到最后一层（num = 1 ）
        # 开始把洋葱还原，返回 num % 2, 有点类似于出栈
        result = binB( num // 2)
        return result + str(num % 2)
    else:
        # 还原到最外面（实际是在剥到最后一片式，还原回去所有的result），出结果
        return result
#字典的用法
>>> 第一种方法
>>> MyDict_1 = dict((('F',70),('C',67),('h',104),('i',105),('s',115)))
>>> MyDict_1['C']
67
>>> 第二种方法
>>> MyDict_2 = {'F':70,'C':67,'h':104,'i':105,'s':115}
>>> MyDict_2['C']
67
>>> 第三种方法
>>> MyDict_3 = dict(F = 70, C = 67, h = 104, i = 105, s = 115)
>>> MyDict_3['C']
67
>>> 第四种方法
>>> MyDict_4 = dict([('F',70),('C',67),('h',104),('i',105),('s',115)])
>>> MyDict_4['C']
67
>>> 第五种方法
>>> MyDict_5 = dict({'F':70,'C':67,'h':104,'i':105,'s':115})
>>> MyDict_5['C']
67
>>> 第六种方法
>>> MyDict_6 = dict(zip(['F', 'C', 'h', 'i', 's'], [70, 67, 104, 105, 115]))
>>> MyDict_6['C']
67
#类                  
#
#
# 实例属性  必须通过初始化或者实例化对象，通过对象去访问，
# 就是每个学生个人 实例=到个体
class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')
print(s.name )

# 类属性  不需要实例化对象，直接通过类名访问
#一类东西 如学生
class Student(object):
    name = 'Student'
print(Student.name)


# 面向对象
# 属性和方法
class Student(object):
    # 初始化方法  self指向创建的实例本身
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

# 实例化对象1
xiaohong = Student('xiaohong',98)
print(id(xiaohong))
# 实例化对象2
xiaobai = Student('xiaobai',81)
print(id(xiaobai))
# 实例化对象3
xiaobai = Student('xiaobai',81)
print(id(xiaobai))
class 智能机器人():             #定义类
    身高 = 168
    体重 = 44                  #定义属性值
    智商 = 198
    def 打招呼():              #定义方法
        print('主人你好！')
    def 卖萌():
        print('主人，求抱抱！')
    def 生气():
        print('主人，我要报警了！')

print('把类的属性打印出来：')
print(智能机器人.身高)         #类调用不同的属性值
print(智能机器人.体重)
print(智能机器人.智商)

智能机器人.打招呼()
智能机器人.卖萌()            #类调用不同的方法
智能机器人.生气()

#结果展示
把类的属性打印出来：
168
44
198
主人你好！
主人，求抱抱！
主人，我要报警了！

#调用类属性
class 智能机器人():
    身高 = 168
    体重 = 44
    智商 = 198
    def 打招呼():
        print('主人你好！')
    def 卖萌():
        print('主人，求抱抱！')
    def 生气():
        print('主人，我要报警了！')
    #@classmethod用来调用类中的属性
    @classmethod        #声明类方法，只有声明之后，才能使用“智能机器人”这个类中的方法
    def 自报信息(cls):   #一定要传入参数cls
        print('主人，我的基础信息有：')
        print('身高：',cls.身高)       #cls.身高 则是在调用类属性
        print('体重：',cls.体重)
        print('智商：',cls.智商)
        print('啦啦啦啦，有没有很喜欢我')
智能机器人.自报信息()
智能机器人.打招呼()       #智能机器人这个类再调用不同的方法
智能机器人.卖萌()
智能机器人.生气()

#结果展示
主人，我的基础信息有：
身高： 168
体重： 44
智商： 198
啦啦啦啦，有没有很喜欢我
主人你好！
主人，求抱抱！
主人，我要报警了！

#调用类方法
class 成绩单():       #定义类
    @classmethod     #声明类方法
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 计算平均分(cls):
        平均分 = (cls.语文_成绩 + cls.数学_成绩)/2
        return 平均分       #因为此方法我们需要调用，所以用return返回结果便于后面的调用

    @classmethod
    def 评级(cls):
        平均分 = cls.计算平均分()        #类方法调用其他的方法
        if 平均分>=90:
            print(cls.学生姓名 + '的评级是：优')
        elif 平均分>= 80 and 平均分<90 :
            print(cls.学生姓名 + '的评级是：良')
        elif 平均分>= 60 and 平均分<80 :
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')

成绩单.录入成绩单()
成绩单.评级()

#结果展示
请输入学生姓名：猫看见
请输入语文成绩：85
请输入数学成绩：76
猫看见的评级是：良

#外部参数
class 加100类():
    def 加100函数(参数):
        总和 = 参数 + 100
        print('计算结果如下：')
        print(总和)
参数 = 1              #外部参数
加100类.加100函数(参数)

#结果展示
计算结果如下：
101

#内部参数
class 加100类():
    def 加100函数(参数):
        总和 = 参数 + 100
        print('计算结果如下：')
        print(总和)
    参数 = 1              #内部参数     
加100类.加100函数(参数)

#结果展示
计算结果如下：
101

#同时传入内部和外部参数
class 加100类():
    变量 = 100       
    
    @classmethod
    def 加100函数(cls,参数):
        总和 = cls.变量 + 参数
        print('加100函数计算结果如下：')
        print(总和)

参数 = int(input('请输入一个整数：'))
加100类.加100函数(参数)

#结果展示
请输入一个整数：25
加100函数计算结果如下：
125

class 基础机器人():
    def __init__(self,参数):
        self.姓名 = 参数

    def 自报姓名(self):
        print('我是' + self.姓名 + '！')     

    def 卖萌(self):
        print('主人，求抱抱！')

class 高级机器人(基础机器人):       #继承
    def 高级卖萌(self):          #新增方法
        print('主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！')

安迪 = 高级机器人('安迪')

安迪.自报姓名()
安迪.卖萌()
安迪.高级卖萌()

#结果展示
我是安迪！
主人，求抱抱！
主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！
#自动打开监控不用时关闭
def file_compare(file1,file2):  
    with open(file1) as f1, open(file2) as f2:  
        count = 0#统计行数  
        differ = []#统计不一样的数量  
 
        for line1 in f1:  
            line2 = f2.readline()  
            count += 1  
            if line1 != line2:  
                differ.append(count)  
    return differ  
#
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:
            print(name + ' : ' + contacts[name])
        except KeyError:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:
            contacts[name] 
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        try:
            del(contacts[name]) # 也可以使用dict.pop()
        except KeyError:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')
#
class Ticket:
    def __init__(self, weekend=False, child=False):
        self.price = 100
        if weekend:
            self.increase = 1.2
        else:
            self.increase = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.price * self.increase * self.discount * num

adult = Ticket()
child = Ticket(child=True)
print("2个大人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))

adult2 = Ticket(weekend=True)
child2 = Ticket(weekend=True, child=True)
print("2个大人 + 1个小孩周末票价为：%.2f" % (adult2.calcPrice(2) + child2.calcPrice(1)))

输出:
2个大人 + 1个小孩平日票价为：250.00
2个大人 + 1个小孩周末票价为：300.00
#有用的东西  组合类
#当一个水池里有多种类用组合
#鳄龟是龟用继承
# 乌龟类
class Turtle:
    def __init__(self, x):
        self.num = x

# 鱼类
class Fish:
    def __init__(self, x):
        self.num = x

# 水池类
class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)  # 把乌龟类实例化组合进来
        self.fish = Fish(y)      # 把鱼类实例化组合进来

    def print_num(self):
        print("水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.print_num()

#偷龙换风  简单
class C2F(float):
    "摄氏度转换为华氏度"
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 1.8 + 32)
#new就是对创建的实例先进行调整在返回实例
class Nint(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)
 #如你所见，访问实例层次上的描述符x，
 #只会返回描述符本身。为了让描述符能够正常工作 
 # #它们必须定义在类的层次上。如果你不这样做，那么Python无法自动
#为你调用__ get__和__ set__方法。
        >>> class MyDes:
    def __init__(self, value = None):
        self.val = value
    def __get__(self, instance, owner):
        return self.val ** 2

    
>>> class Test:
    def __init__(self):
        self.x = MyDes(3)

        
>>> test = Test()
>>> test.x
>>> >>> test.x
<__main__.MyDes object at 0x000001A2EA668278>