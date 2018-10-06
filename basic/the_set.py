#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = set([1, 1, 2, 2, 2, 2, 3, 3, 4])
s.add(3)
s.add(4)
print('s=', s)
s.remove(4)
print('s=', s)

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print('s1 & s2 =', s1 & s2)
print('s1 | s2 =', s1 | s2)
