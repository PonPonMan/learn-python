#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = "盆盆好帅"
print(s)
s_encode = s.encode("utf-8")
print(s_encode)
print(s_encode.decode("utf-8"))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print("小明的成绩比去年提升了 %.2f%%" % r)
