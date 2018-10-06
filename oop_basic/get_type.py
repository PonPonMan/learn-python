#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()

import types

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

print('type(\'abc\')==str?', type('abc') == str)


def fn():
    pass


print('type(fn)==types.FunctionType?', isinstance(fn, types.FunctionType))
