# 装饰器的学习
# ###
import time


class Test():
    _Num = 0

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Value):
        if Value > 50:
            self._Num = 50
        elif Value < -50:
            self._Num = -50
        else:
            self._Num = Value


# 迭代器与可迭代对象的学习
# ###
class Iter_Test_1:
    def __init__(self, Lst=[]):
        self.Lst = Lst

    def __iter__(self):
        return iter(self.Lst)


class Iter_Test_2:
    def __init__(self, Lst=[]):
        self.Lst = Lst
        self._Index = 0

    def __iter__(self):
        return iter(self.Lst)

    def __next__(self):
        if self._Index < len(self.Lst):
            Num = self.Lst[self._Index]
            self._Index += 1
            return Num
        else:
            self._Index = 0
            raise StopIteration


# 类装饰器的学习
# ###
class Check_Time:
    def __init__(self, Func):
        self.Func = Func

    def __call__(self, *args, **kwargs):
        Start_Time = time.time()
        Res = self.Func(*args, **kwargs)
        print('运行时间为：{}'.format(time.time() - Start_Time))
        return Res


@Check_Time
def Func_Test(*args):
    Sum = 2
    for i in args:
        if i == 1:
            continue
        else:
            Sum = Sum ** i
    return Sum
