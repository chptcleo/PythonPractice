'''
Created on 2019年5月17日

@author: chenhuaping
'''


def cal(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s


if __name__ == '__main__':
    list1 = (1, 3, 5)
    print(cal(*list1))
    list2 = [1, 2, 3]
    print(cal(*list2))
