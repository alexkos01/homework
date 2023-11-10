import sqlite3

with sqlite3.connect('data.db') as db:
    cur = db.cursor()
    cur.execute('''create table if not exists people(name text, profession text, age integer)''')
    cur.execute('''insert into people values('Александр', 'менеджер', 25), ('Максим', 'учитель', 30), ('Олег', 'строитель', 32)''')



