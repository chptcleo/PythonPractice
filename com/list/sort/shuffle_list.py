'''
@author: chenhuaping
'''
import random

def shuffle(a_list):
    random.shuffle(a_list)
    print(a_list)

if __name__ == '__main__':
    a_list = [1,2,3,4,5]
    shuffle(a_list)
