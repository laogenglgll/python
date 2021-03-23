#28 29 30 一个题
#!/usr/bin/python
# -*- coding:utf-8 -*-

import time as t


class MyTimer:
    def __init__(self, func, number=1000000):
        self.prompt = "未开始计时"
        self.lasted = 0.0
        self.default_timer = t.perf_counter
        self.func = func
        self.number = number
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" % result
        return prompt
    # 内置方法，计算运行时间
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):
            self.func()
        self.end = self.default_timer()
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了 %0.2f 秒" % self.lasted

    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效")

def test():
    text = "I love FishC.com!"
    char = 'o'
    if char in text:
        pass



t1 = MyTimer(test)
t1.timing()
print(t1)
t2 = MyTimer(test, 100000000)
t2.timing()
print(t2)
# 另一种

#!/usr/bin/python
# -*- coding:utf-8 -*-

import time as t


class MyTimer:
    def __init__(self):
        self.prompt = "未开始计时"
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了%0.2f秒" % result
        return prompt
    def start(self):
        self.begin = self.default_timer()
        self.prompt = "提示：请先调用stop()停止计时！"
        print("计时开始！")
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()运行计时！")
        else:
            self.end = self.default_timer()
            self._calc()
            print("计时结束")
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了%0.2f秒" % self.lasted
        print(self.prompt)
        self.begin = 0
        self.end = 0

    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效")



t1 = MyTimer()
t1.set_timer('perf_counter')
t1.start()
t.sleep(5.2)
t1.stop()
t2 = MyTimer()
t2.set_timer('perf_counter')
t2.start()
t.sleep(5.2)
t2.stop()
print(t1 + t2)