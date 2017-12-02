import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        return '0'
    return value

def insert_data():
    conn = sqlite3.connect('food.db')
    curs = conn.cursor()
    curs.execute('drop table food')
    curs.execute('''
    CREATE TABLE food (
    id TEXT PRIMARY KEY,
    desc TEXT,
    water FLOAT,
    kcal FLOAT,
    protein FLOAT,
    fat FLOAT,
    ash FLOAT,
    carbs FLOAT,
    fiber FLOAT,
    sugar FLOAT,
    price1 FLOAT,
    price2 FLOAT,
    price3 FLOAT,
    price4 FLOAT
    )
    ''')
    
    query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    
    for line in open('FOOD_DES.txt'):
        fields = line.split('^')
        vals = [convert(val) for val in fields]
        curs.execute(query, vals)
    
    conn.commit()
    conn.close()
    
def query_data():
    conn = sqlite3.connect('food.db')
    curs = conn.cursor()
    query = 'select * from food where price4>5'
    curs.execute(query)
#     names = [f[0] for f in curs.description]
    for row in curs.fetchall():
        print row
#         for pair in zip(names, row):
#             print '%s: %s' % pair
            
    conn.close()

if __name__ == '__main__':
#     insert_data()
    query_data()