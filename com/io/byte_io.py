'''
@author: Administrator
'''
# -*- coding: utf-8 -*-
from io import BytesIO

def write_io():
    b_io = BytesIO()
    b_io.write('����'.encode('utf-8'))
    print(b_io.getvalue())


if __name__ == '__main__':
    write_io()