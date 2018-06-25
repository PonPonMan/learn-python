#!/usr/bin/env python3
# -*- coding: utf-8 -*-

step = 0


def move(p1, p2):
    global step
    step = step + 1
    print('step' + str(step)+':', p1, '-->', p2)


def hanoi(n, a, b, c):
    if n == 1:
        move(a, c)
    else:
        hanoi(n - 1, a, c, b)
        # print(a, '-->', b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


hanoi(4, 'A', 'B', 'C')
