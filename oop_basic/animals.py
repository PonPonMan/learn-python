#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    pass


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
cat = Cat()

dog.run()
cat.run()

run_twice(dog)
