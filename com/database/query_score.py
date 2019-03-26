'''
@author: chenhuaping
'''
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

connection = sqlite3.connect(db_file)
cursor = connection.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
connection.commit()
connection.close()


def get_score_in(low, high):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('select name from user where score between ? and ?', (low, high))
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students


if __name__ == '__main__':
    students = get_score_in(60, 80)
    print(students)
