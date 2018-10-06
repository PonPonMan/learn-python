#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'PonPonMan'

import sys


def _private_1():
    return 'Hello world'


def _private_2(name):
    return 'Hello, %s' % name


def _private_3(name):
    return 'Hi, %s' % name


def greeting(name=None):
    if name is None:
        return _private_1()
    if len(name) > 3:
        return _private_3(name)
    else:
        return _private_2(name)


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print(greeting())
    elif len(args) == 2:
        print(greeting(args[1]))
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
