#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Bart', 'Lisa', 'Adam']

n = 0
while n < 3:
    print("hello", L[n])
    n += 1

n = 0
while n < 1000:
    n += 1
    if n % 2 == 1:
        continue
    if n > 10:
        break
    print(n)
