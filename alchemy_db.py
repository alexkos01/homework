import sqlalchemy as db

engine = db.create_engine(('sqlite:///my_date.db'))
con = engine.connect()
metadata = db.MetaData()

words = db.Table('words', metadata, db.Column('word', db.Text))
nums = db.Table('nums', metadata, db.Column('num', db.Integer))

metadata.create_all(engine)

def add_word_table(w):
    con.execute(words.insert().values([{'word': w}]))
    con.execute(nums.insert().values([{'num': len(w)}]))
    con.commit()


def add_num_table(n):
    if n % 2 == 0: con.execute(nums.insert().values([{'num': n}]))
    else: con.execute(words.insert().values([{'word': 'нечётное'}]))
    con.commit()

sp = [10, 'two', 'world', 7, 'black', 15, 'hi']

[add_word_table(i) if type(i) is str else add_num_table(i) for i in sp]

con.close()