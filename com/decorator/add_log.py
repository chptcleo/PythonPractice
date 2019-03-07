# -*- coding: utf-8 -*-
'''
Created on 2019��3��5��

@author: Administrator
'''
import time
import functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, time.asctime()))
        return fn(*args, **kw)
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z


if __name__ == '__main__':
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')
