#!/usr/bin/env python3
# -*- coding: utf-8 -*-

step = 0


def move(p1, p2):
    global step
    step = step + 1
    print('step' + str(step) + ':', p1, '-->', p2)


def hanoi(n, a, b, c):
    if n == 1:
        move(a, c)
    else:
        # 先把第n-1个盘子移动到b
        hanoi(n - 1, a, c, b)
        # print(a, '-->', b)
        # 再把最后一个盘子移动到c
        hanoi(1, a, b, c)
        # 把b上的盘子移动到c
        hanoi(n - 1, b, a, c)


hanoi(4, 'A', 'B', 'C')
