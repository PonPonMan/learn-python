#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()
s.name = 'Micheal'
s.age = 25
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score:', g.score)
