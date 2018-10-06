#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# List

import os

listcompr1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(listcompr1)

listcompr2 = [m + n for m in 'ABC' for n in 'XYZ']
print(listcompr2)

# .是指当前目录
listcompr3 = [d for d in os.listdir('.')]
print(listcompr3)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
listcompr4 = [k + '=' + v for k, v in d.items()]
print(listcompr4)

L = ['Hello', 'World', 'IBM', 'Apple']
listcompr5 = [s.lower() for s in L]
print(listcompr5)

# 练习:
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')