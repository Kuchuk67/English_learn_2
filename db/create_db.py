import sqlite3
import os

def create_db():
    # Подключение к базе данных (если файла нет — он будет создан)
    filename_db = "dictionary.db"
    filename_db = os.path.abspath(filename_db)

    conn = sqlite3.connect(filename_db)

    # Курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    # Создание таблицы word
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS word (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT(50),
        translate TEXT(50),
        example TEXT(50),
        rate INTEGER,
        dictionary INTEGER
    )
    """)
    # Сохраняем изменения
    conn.commit()

    # Создание таблицы 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dictionary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT(50)
    )
    """)

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение
    conn.close()

    print("Таблицы успешно созданы")