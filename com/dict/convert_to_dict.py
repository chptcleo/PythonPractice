'''
Created on 2019年3月25日

@author: chenhuaping
'''

if __name__ == '__main__':
    str1 = 'k:1|k1:2|k2:3|k3:4'
    dict1 = {}
    for item in str1.split('|'):
        key, value = item.split(':')
        dict1[key] = value
    print(dict1)