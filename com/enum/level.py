'''
Created on 2019年5月21日

@author: chenhuaping
'''

from enum import Enum, unique


def execute(my_enum):
#     level = Enum('level', ('junior', 'media', 'senior'))
    for name, member in my_enum.__members__.items():
        print('%s, %s, %s' % (str(name), str(member), str(member.value)))

    
@unique    
class Color(Enum):
    blue = 1
    white = 2
    red = 3


if __name__ == '__main__':
    level = Enum('level', ('junior', 'media', 'senior'))
    execute(level)
#     the_color = Color()
    execute(Color)
