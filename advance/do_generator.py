#!/usr/bin/env python3
# -*- coding: utf-8 -*-

g = (x * x for x in range(1, 3))
for n in g:
    print(n)


# Fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(6)

for n in g:
    print(n)

g = fib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4,
                                                      1], [1, 5, 10, 10, 5, 1],
               [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7,
                                          1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
               [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
    print('测试通过!')
else:
    print('测试失败!')
