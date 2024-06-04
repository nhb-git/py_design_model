#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  : py_design_model
# @Time     : 2024/5/29 上午7:05
# @Author   : niuhaibao
# @File     : main.py
# @IDE      : PyCharm
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Dog'


class Cat(Animal):
    def speak(self):
        return 'Cat'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'Dog':
            return Dog()
        if animal_type == 'Cat':
            return Cat()
        return Dog()


def client(animal):
    return animal.speak()


if __name__ == '__main__':
    animal = AnimalFactory.create_animal('Dog')
    print(client(animal))

    animal = AnimalFactory.create_animal('Cat')
    print(client(animal))
