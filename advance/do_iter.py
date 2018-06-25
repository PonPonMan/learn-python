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
