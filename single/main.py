#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  : py_design_model
# @Time     : 2024/6/2 下午9:17
# @Author   : niuhaibao
# @File     : main.py
# @IDE      : PyCharm
from threading import Lock


class SingletonMeta(type):
    """
    单例元类
    """
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


if __name__ == '__main__':
    s = Singleton()
    s1 = Singleton()
    if id(s) == id(s1):
        print("s and s1 are the same instance")
    else:
        print("s and s1 are different instances")
