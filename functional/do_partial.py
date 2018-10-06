#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

# 相当于
# kw = { 'base': 2 }
# int('10010', **kw)

print(int2('1001'))

max2 = functools.partial(max, 10)

# 相当于
# args = (10, 5, 6, 7)
# max(*args)

print(max2(5, 6, 7))
