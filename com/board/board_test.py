import psycopg2

conn = psycopg2.connect(database='postgres', user='postgres', password='NCEP1pr2!')
curs = conn.cursor()
curs.execute('select * from pg_am')
print curs.fetchall()