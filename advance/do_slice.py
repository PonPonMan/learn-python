#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
print(L[:5])
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[10:20:2])
print(L[::5])
print(L[:])

print('ABCDEFG' [:3])
print('ABCDEFG' [::2])


def trim(s):
    if s == '':
        return ''
    if s[0] == ' ':
        return trim(s[1:])
    if s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
