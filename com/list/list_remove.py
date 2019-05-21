

if __name__ == '__main__':
    list1 = [5,3,7,2,9,1,8]
    print(id(list1))
    list2 = list1[:]
    print(list2)
    print(id(list2))
    list_length = len(list1)
    for i in range(list_length-1):
        tmp = list1[-1-i]
        print(tmp)
        if tmp > 5:
            pass
        else:
            list1.remove(tmp)
    print(list1)
