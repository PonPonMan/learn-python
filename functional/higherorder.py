#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数英文叫Higher-order function
# 变量可以指向函数

f = abs
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

