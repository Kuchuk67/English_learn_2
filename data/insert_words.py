#import sys
import sqlite3
import os
from trip.d_1 import d_1

#print(sys.argv[1])
#words = d_1()
dictionary = 1

# Подключение к БД
conn = sqlite3.connect("dictionary.db")
cursor = conn.cursor()

# SQL-запрос на вставку
insert_sql = """
INSERT INTO word (word, translate, example, rate, dictionary)
VALUES (?, ?, ?, ?, ?)
"""

# Подготовка данных (rate = 0, dictionary = 1)
data_to_insert = [
    (word, translate, example, 0, dictionary)
    for word, translate, example in words
]

# Массовая вставка
cursor.executemany(insert_sql, data_to_insert)

# Сохраняем изменения
conn.commit()
conn.close()

print("Данные успешно добавлены в таблицу 'word'")
