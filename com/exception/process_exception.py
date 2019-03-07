from functools import reduce


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    try:
        ns = map(str2num, ss)
    except ValueError as ve:
        print("Value Error:" + str(ve))
        
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    try:
        r = calc('99 + 88 + 7.6')
    except UnboundLocalError as ul:
        print("UnboundLocalError:" + str(ul))
    print('99 + 88 + 7.6 =', r)


main()
