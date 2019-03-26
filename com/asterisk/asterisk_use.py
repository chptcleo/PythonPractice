'''
@author: chenhuaping
'''
import sys

def exec1():
    players = ['kobe', 'james', 'wade']
    print(players[0], players[1], players[2])
    print(players)
    print(sys.version_info)
#     print(*players)


if __name__ == '__main__':
    exec1()
