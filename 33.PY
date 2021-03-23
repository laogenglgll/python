#__ iter__()：返回迭代器本身；
#__ next__()：这里写迭代的规律
import datetime as dt
class IteR:
    def __iter__(self):
        return self
class YeaR:
    def __init__(self,before):
        self.now = dt.date.today().year
        self.before = before
        self.c=[]
    def RyeaR(self,year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
    def years(self):
        
        a=list(range(self.before,self.now))
        for b in a:
            if self.RyeaR(b):
                self.c.append(b)
            else:
                pass
        self.c=iter(self.c)
        return self.prin()
        
    def itER(self):
        pass
    def __iter__(self):
            return self
    def prin(self):
        for i in self.c:

            print(i)
        self.c=iter(self.c)

        
    
year=YeaR(2000)

print(year.years())#迭代器应该没重现更新 所以还是结束时后的样子
year.prin()
#无法重置迭代器
#import 模块名 as  新名字 #调用模块时比较好用

 