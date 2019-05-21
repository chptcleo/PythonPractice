'''
Created on 2019年4月3日

@author: chenhuaping
'''
from types import new_class


def sort_list(list_str):
    
    new_list_str = sorted(list_str, key=lambda x: x, reverse=True)
    print(list_str)
    print(new_list_str)
    for i in range(len(new_list_str)):
        if int(new_list_str[i]) % 2 != 0:
            new_list_str.insert(0, new_list_str.pop(i))
    print(new_list_str)
    

if __name__ == '__main__':
    list_str = '1982376455'
    sort_list(list_str)
