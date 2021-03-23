#思考这一讲学习的内容，请动手在一个类中定义一个变量，用于跟踪类有多少个实例被创建
# （当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）。
class Stack():
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):  # 判断是否为空
        return not self.stack

    def push(self, obj):  # 入栈
        print("成功入栈数据：", obj)
        self.stack.append(obj)

    def pop(self):  # 出栈
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("成功出栈数据：", self.stack[-1])
            return self.stack.pop()

    def top(self):  # 显示第一个栈顶数据
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("栈顶数据为：", end="")
            return self.stack[-1]

    def bottom(self):  # 显示栈底数据
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("栈底数据为：", end="")
            return self.stack[0]

    def showStack(self): # 展示栈内的所有数据（自己附加上去的方法，为了方便看栈内还有哪些数据）
        print("目前栈内的所有数据为：", end="")
        return self.stack[:]


s = Stack([])
print(s.isEmpty())  # True
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
print(s.showStack())
print(s.top())  # 栈顶是5
s.pop()  # 5被弹出，栈顶变成4
print(s.showStack())
print(s.top())
print(s.bottom())
