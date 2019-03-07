#coding:utf-8
'''
Created on 2019年3月5日

@author: Administrator
'''


def normalize(name):
    return name[0].upper() + name[1:].lower()


if __name__ == "__main__":
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
