'''
@author: chenhuaping
'''
import datetime


def count():
    year = input('input year: ')
    month = input('input month: ')
    day = input('input day: ')
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    print(date1)
    date2 = datetime.date(year=int(year), month=1 , day=1)
    print(date2)
    return (date1 - date2).days + 1


if __name__ == '__main__':
    print(count())
