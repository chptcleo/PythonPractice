# -*- coding: utf-8 -*-
'''
Created on 2019��3��5��

@author: Administrator
'''

def create_counter():
    
    def counter():
        x = 0
        return x+1
    return counter

if __name__ == '__main__':
    
    counter_a = create_counter()
    print(counter_a(), counter_a(), counter_a(), counter_a(), counter_a())
    counter_b = create_counter()
    if [counter_b(),counter_b(),counter_b(),counter_b()] == [1,2,3,4]:
        print("pass")
    else:
        print("fail")