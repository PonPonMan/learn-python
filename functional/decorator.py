#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import functools
from datetime import datetime

# def log(func):
#     def warpper(*args, **kw):
#         @functools.wraps(func)
#         print('call %s()' % func.__name__)
#         return func(*args, **kw)

#     return warpper

# @log
# def now():
#     print(datetime.now().date())

# now()


def log(text=None):
    def decorator(func):
        @functools.wraps(func)  # 不加这个调用函数的__name__会变为warpper
        def warpper(*args, **kw):
            nonlocal text
            if text is None:
                text = 'call'
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)

        return warpper

    return decorator


@log('execute')
def now():
    print(datetime.now().date())


@log()
def now2():
    print(datetime.now().date())


now()
print(now.__name__)
now2()


# 练习
def metric(func):
    def warpper(*args, **kw):
        start_time = time.time()
        fn = func(*args, **kw)
        end_time = time.time()
        print('%s executed in %s ms' % (func.__name__, end_time - start_time))
        return fn

    return warpper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
