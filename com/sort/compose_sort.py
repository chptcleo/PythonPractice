'''

@author: Administrator
'''


def compose_sort(list1, list2):
    list3 = list()
    list3.extend(list1)
    list3.extend(list2)
    list_length = len(list3)
    for i in range(list_length):
        for j in range(list_length - i - 1):
            if list3[j] > list3[j + 1]:
                tmp = (list3[j], list3[j + 1])
                list3[j] = tmp[1]
                list3[j + 1] = tmp[0]
    print(list3)
    


if __name__ == '__main__':
    list1 = [1, 3, 4]
    list2 = [1, 2, 4]
    compose_sort(list1, list2)
