#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Closure 闭包


def count():
    def f(j):
        return lambda: j * j

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 练习
# def createCounter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter


# 解法2
def countGenerator():
    n = 0
    while True:
        n += 1
        yield n


def createCounter():
    it = countGenerator()

    def counter():
        return next(it)

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
