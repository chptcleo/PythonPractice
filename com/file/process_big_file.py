'''
@author: chenhuaping
'''
import os


def get_lines(big_file):
    with open(big_file,'rb') as f:
        return f.readlines()


if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    big_file = os.path.join(current_dir, 'Hello.flac')
    print(big_file)
    for content in get_lines(big_file):
        print(content)