'''
@author: chenhuaping
'''


def get_index(list1, sum_num):
    list_length = len(list1)
    for i in range(list_length):
        for list_item in list1[i + 1:]:
            plus_result = list1[i] + list_item
            if sum_num == plus_result:
                return (i, list1.index(list_item)) 


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 17
    print(get_index(nums, target))
