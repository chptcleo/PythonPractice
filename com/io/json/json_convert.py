# -*- coding: utf-8 -*-

import json


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

def dict2student(d):
    return Student(d['name'],d['age'])

def dumps_test():
    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=False)
    print(s)


if __name__ == '__main__':
    dumps_test()
    s = Student('domi', 3)
    json_str = json.dumps(s, default=lambda obj:obj.__dict__)
    print(json_str)
    s2 = json.loads(json_str, object_hook = dict2student)
    print(s2.name)
