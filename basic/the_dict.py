#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
print(d['Micheal'])
d['Micheal'] = 90
print(d['Micheal'])
if 'Thomas' in d:
    print(d['Thomas'])
else:
    print("%s not in dict" % 'Thomas')
d.pop('Bob')
print(d)
