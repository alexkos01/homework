# У вас есть текстовый файл со списком студентов, где информация записана: (номер в журнале) Имя Фамилия Отчество оценка
#  (номер в журнале) Имя Фамилия Отчество оценка (номер в журнале) Имя Фамилия Отчество оценка1.Сформулируйте SQL
# запрос для создания таблицы students.  Поля: student_id, name TEXT,  surname TEXT, patronymic TEXT, rating INT2.Создать функции:
# 1. Вставить данные учеников в таблицу     2. Получения данных обо всех студентах
# 3. Получения данных об одном студенте по id     0. Выход3. Функции вызывать в цикле, чтоб у пользователя был выбор.

import sqlite3 as sq

with open('students.txt', 'w+', encoding='utf-8') as f:
    for i in range(2): f.writelines(input() + '\n')


with sq.connect('school.db') as db:
    cur = db.cursor()
    cur.execute('''create table if not exists students(student_id integer primary key autoincrement,
    name text, surname text, patronymic text, rating integer)
    ''')


def set_data_students():
    with open('students.txt', 'r+', encoding='UTF-8') as f:
        for i in f.readlines():
            ls = i.split()
            cur.execute('''insert into students (name, surname, patronymic, rating) values (?, ?, ?, ?)''',
                        (ls[1], ls[2], ls[3], ls[4]))
            db.commit()


def get_data_all_students():
    r = cur.execute('''select * from students''')
    for i in r.fetchall(): print(*i)


def set_data_single_students(s):
    r = cur.execute('''select * from students where student_id=?''', (s,))
    print(*[i for i in r.fetchone()])


while True:
    user_choice = int(input('''
1 - вставить данные учеников таблицу
2 - получение данных обо всех студентах
3 - получение данных об одном студенте
0 - выход
'''))
    if user_choice == 1: set_data_students()
    elif user_choice == 2: get_data_all_students()
    elif user_choice == 3: set_data_single_students(int(input('введите id ученика\n')))
    elif user_choice == 0: break
