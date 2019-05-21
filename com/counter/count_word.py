'''
Created on 2019年3月28日

@author: chenhuaping
'''
import os


def count_word(file1):
    kv = {}
    with open(file1) as f:
        while True:
            line = f.readline()
            if line:
                words = line.split()
                for word in words:
                    if word in kv.keys():
                        kv[word] = kv[word] + 1
                    else:
                        kv[word] = 1
            else:
                break
    return sorted(kv.items(), key=lambda x:x[1], reverse=True)[:10]
     

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, 'test_txt')
    print(count_word(file1))
