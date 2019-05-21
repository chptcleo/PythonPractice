'''
Created on 2019年3月28日

@author: chenhuaping
'''

def get_special_number(list1):
    res_list = []
    for i in list1:
        if i%2 == 0 and list1.index(i)%2 ==0:
            res_list.append(i)
    return res_list

if __name__ == '__main__':
    list1 = [0,1,2,3,4,5,6,7,8,9,10]
    print(get_special_number(list1))