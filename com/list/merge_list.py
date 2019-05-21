'''
Created on 2019年3月28日

@author: chenhuaping
'''

def merge_list(list1, list2):
    res_list = []
    while len(list1) >0 and len(list2)>0:
        if list1[0] < list2[0]:
            res_list.append(list1[0])
            list1.pop(0)
        else:
            res_list.append(list2[0])
            list2.pop(0)
    return res_list
        

if __name__ == '__main__':
    list1 = [1,4,5,7,9]
    list2 = [1,2,3,5,6]
    print(merge_list(list1, list2))