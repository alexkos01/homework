import sqlite3

con = sqlite3.connect('my_data.db')
c = con.cursor()
c.execute('''create table text_data(txt_values text)''')
c.execute('''create table int_data(int_values integer)''')


def add_word_table(w):
    c.execute('''insert into text_data(txt_values) values (?)''', (w,))
    c.execute('''insert into int_data(int_values) values (?)''', (len(w),))
    con.commit()

def add_num_table(n):
    if n % 2 == 0: c.execute('''insert into int_data(int_values) values (?)''', (n,))
    else: c.execute('''insert into text_data(txt_values) values ('нечётное')''')
    con.commit()


sp = [10, 'two', 'world', 7, 'black', 15, 'hi']

[add_word_table(i) if type(i) is str else add_num_table(i) for i in sp]