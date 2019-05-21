'''
@author: Administrator
'''
import threading


class Student(object):
    
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name


def process_thread(name):
    thead_local.student = Student(name)
    process_student()

    
def process_student():
    print('This is %s in %s' % (thead_local.student.get_name(), threading.current_thread()))


if __name__ == '__main__':
    thead_local = threading.local()
    thread1 = threading.Thread(target=process_thread, args=('kobe',), name='thread1')
    thread2 = threading.Thread(target=process_thread, args=('james',), name='thread2')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
