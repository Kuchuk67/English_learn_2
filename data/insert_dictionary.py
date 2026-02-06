import sys
import sqlite3
import os

# запуск скрипта
# python data/insert_dictionary.py 1 "Words for polite conversations"

def insert_dictionary(dictionary_id:int, dictionary_name:str)->None:

    # Подключение к БД
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()

    # SQL-запрос на вставку
    insert_sql = """
    INSERT INTO dictionary (id, name)
    VALUES (?, ?)
    """

    # Массовая вставка
    cursor.executemany(insert_sql, [(dictionary_id, dictionary_name)])

    # Сохраняем изменения
    conn.commit()

    print("Данные успешно добавлены в таблицу 'dictionary'")

    # Получаем все записи из таблицы word
    cursor.execute("SELECT * FROM dictionary")
    rows = cursor.fetchall()

    # Выводим результаты
    for row in rows:
        print(row)
    conn.close()


dictionary_id = int(sys.argv[1])
dictionary_name = sys.argv[2]
insert_dictionary(dictionary_id, dictionary_name)