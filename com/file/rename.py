# -*- coding: utf-8 -*-
'''
Created on 2017��6��18��

@author: Administrator
'''
import os

def get_files(path, file_list1):
    files = os.listdir(path)
    for file in files:
        full_path =  os.path.join(path, file)
        if os.path.isdir(full_path):
            get_files(full_path, file_list1)
        if not os.path.isdir(full_path):
            file_list1.append(full_path)

def rename(file_list1):
    for file in file_list1:
        dot_index = file.rfind('.')
        file_type = file[dot_index:]
        file_name = file[:dot_index]
        line_index = file_name.rfind('-')
        if line_index == -1:
            continue
        new_file_name = file_name[:line_index]
        new_file_name = new_file_name.rstrip()
        print file, new_file_name+file_type
        os.rename(file, new_file_name+file_type)
        
if __name__ == '__main__':
    path1 = 'E:\Music\music'
    file_list1 = []
    get_files(path1, file_list1)
    print len(file_list1)
    rename(file_list1)
    