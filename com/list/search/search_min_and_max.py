'''
@author: Administrator
'''


def find_min_and_max(L):
    
    list_length = len(L)
    if(list_length == 0):
        return None,None
    for i in range(list_length):
        for j in range(list_length - i - 1):
            if(L[j] > L[j + 1]):
                tmp = (L[j], L[j + 1])
                L[j] = tmp[1]
                L[j + 1] = tmp[0]
    print "L:",  L
    return L[0], L[list_length - 1]


if __name__ == '__main__':
    
    if find_min_and_max([]) != (None, None):
        print('fail!')
    elif find_min_and_max([7]) != (7, 7):
        print('fail!')
    elif find_min_and_max([7, 1]) != (1, 7):
        print('fail!')
    elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
        print('fail!')
