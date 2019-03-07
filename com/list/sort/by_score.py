# -*- coding: utf-8 -*-
'''
Created on 2019Äê3ÔÂ5ÈÕ

@author: Administrator
'''
def by_score(t):
    return t[1],t[0]

if __name__ == '__main__':
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key= by_score)
    print(L2)
    