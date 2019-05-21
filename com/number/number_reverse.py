'''

@author: chenhuaping
'''


def reverse(number1):
    str_number1 = str(number1)
    list_number = []
    if str_number1[0] == '-':
        list_number.append('-')
        for i in range(1, len(str_number1)): 
            list_number.append(str_number1[-i])
    else:
        for i in range(1, len(str_number1) + 1):
            list_number.append(str_number1[-i])
    return int(''.join(list_number))


if __name__ == '__main__':
    print(reverse(123))
