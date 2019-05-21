'''
@author: chenhuaping
'''


def compose():
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if a != b and b != c and c != a:
                    print('%d%d%d' % (a, b, c))


if __name__ == '__main__':
    compose()
