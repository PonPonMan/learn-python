#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))

# str2int

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def str2int(s):
    # def fn(x, y):
    #     return x * 10 + y
    def str2num(s):
        return DIGITS[s]

    return reduce(lambda x, y: x * 10 + y, map(str2num, s))


print(str2int('12345'))


# 练习1
def prod(L):
    return reduce(lambda x, y: x * y, L)


# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习
def str2float(str):
    ss = str.split('.')

    def str2num(s):
        return DIGITS[s]

    def fn(x, y):
        return (x * 10 + y)

    return reduce(fn, map(
        str2num,
        ss[0])) + reduce(fn, map(str2num, ss[1])) / pow(10, len(ss[1]))


# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
