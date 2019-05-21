'''

@author: chenhuaping
'''

if __name__ == '__main__':
    list1 = ['b', 'c', 'd', 'c', 'a', 'a']
    list2 = list(set(list1))
    print(list2)
    print(sorted(list2, key=lambda x: x))
    print(complex(1.1))
