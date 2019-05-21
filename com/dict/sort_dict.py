'''
@author: chenhuaping
'''

if __name__ == '__main__':
    a_dict = {'a':24, 'g':52, 'i':12, 'k':33}
    print(sorted(a_dict.items(), key = lambda x:x[1]))
    print(a_dict)
    list1 =  [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
    print(sorted(list1, key = lambda x: x['age'], reverse = True))
