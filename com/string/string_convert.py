'''

@author: chenhuaping
'''


def convert2int(str_num):
    int_num = 0
    for i in str_num:
        for j in range(10):
            if i == str(j):
                int_num = int_num * 10 + j
    print(int_num)

if __name__ == '__main__':
    convert2int('564')
