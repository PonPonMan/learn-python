#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
        111, 121, 131, 141, 151, 161, 171, 181, 191
]:
    print('测试成功!')
else:
    print('测试失败!')
