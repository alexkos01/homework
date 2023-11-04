# 1.Сформулируйте SQL запрос для создания таблицы movies.
# Поля:
# movie_id, name TEXT, release_year INTEGER, genre TEXT
# 2. Создать функции:
#  1. Добавить фильм (заполнение делать с клавиатуры)
#  2. Получения данных обо всех фильмах
#  3. Получения данных об одном фильме по id
#  0. Выход
# 3. Функции вызывать в цикле, чтоб у пользователя был выбор

import sqlite3

connect = sqlite3.connect('testing.db')
cursor = connect.cursor()
cursor.execute('''select*from books''')
cursor.execute(
    '''create table if not exists movies(movie_id integer primary key autoincrement, name text, release_year integer, genre text)''')


def set_data_movie(name, release_year, genre):
    cursor.execute('''insert into movies(name, release_year, genre) values (?, ?, ?)''',
                   (name, release_year, genre))
    connect.commit()


def get_data_movies():
    cursor.execute('''select*from movies''')
    for i in cursor.fetchall(): print(*i)


def get_single_movie(r):
    cursor.execute('''select*from movies where movie_id=? ''', (r,))
    for i in cursor.fetchall(): print(*i[1:])


def close_date_movies():
    connect.close()


while True:
    user_inp = int(input('1 - Внесение в таблицу нового фильма\n2 - Вывод информации о всех фильмах в таблице\n'
                         '3 - Вывод информации по id одного фильма\n0 - Выход из программы\n'))
    if user_inp == 1:
        set_data_movie(input('введите название фильма\n'), int(input('введите дату выходна на экран\n')),
                       input('введите название жанра\n'))
    elif user_inp == 2:
        get_data_movies()
    elif user_inp == 3:
        get_single_movie(int(input('введите id списка\n')))
    elif user_inp == 0:
        close_date_movies()
        break
