# -*- coding: utf-8 -*-
'''
Created on 2019��3��5��

@author: Administrator
'''
def is_palindrome(n):
    str_n = str(n)
    half_length = len(str_n)/2
    for i in range(half_length):
        if str_n[i] != str_n[len(str_n)-1-i]:
            return False
    return True

if __name__ == '__main__':
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')