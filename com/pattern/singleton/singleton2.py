'''
@author: chenhuaping
'''


def singleton(cls):
    instances = {}

    def wrapper(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return wrapper

    
@singleton
class Foo(object):
    pass


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print(foo1 is foo2)
