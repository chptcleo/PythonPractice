'''

@author: chenhuaping
'''

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    for item in list2:
        if list1.count(item) > 0:
            print(item)
