#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

# 验证对象是否为可迭代的对象，可迭代对象可以用for...in...
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
for ch in 'ABC':
    print(ch)

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax(L):
    if L is None or L == []:
        return (None, None)
    minValue = maxValue = L[0]
    for i in L:
        minValue = min(minValue, i)
        maxValue = max(maxValue, i)
    return (minValue, maxValue)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

for x in [1, 2, 3, 4, 5]:
    print(x)

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        print(next(it))
    except StopIteration:
        break
