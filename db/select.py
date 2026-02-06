import sqlite3
import random


def words_for_practic(dictionary_id)->list:
    """
    Получаем слова с минимальным рейтингом для урока из указанного ID словаря
    """
    # Подключение к базе данных
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # Получаем все записи из таблицы word
    query = """
        SELECT * FROM word  
        WHERE dictionary = ? 
        AND  rate = (SELECT MIN(rate) FROM word WHERE dictionary = ?);
    """
    cursor.execute(query, (dictionary_id, dictionary_id))
    rows = cursor.fetchall()
    # Закрываем соединение
    conn.close()
    return rows

def word_for_practic(dictionary_id, rate)->list:
    """
    Получаем одно слово с указанным рейтингом для урока из указанного ID словаря
    """
    # Подключение к базе данных
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # Получаем все записи из таблицы word
    query = """
        SELECT * FROM word  
        WHERE dictionary = ? 
        AND  rate = ? 
        LIMIT 10;
    """
    cursor.execute(query, (dictionary_id, rate))
    rows = cursor.fetchall()
    # Закрываем соединение
    conn.close()
    random.shuffle(rows)
    if len(rows)>0:
        return rows[0]
    else:
        return []


def list_dictionary()->list:
    """
    Получаем список словарей
    """
    # Подключение к базе данных
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # Получаем все записи из таблицы word
    query = """
        SELECT * FROM dictionary ;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    # Закрываем соединение
    conn.close()
    return rows

def min_rate(dictionary_id:int) -> int:
    """
    Получаем минимальный рейтинг для  указанного ID словаря
    """
    # Подключение к базе данных
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # Получаем все записи из таблицы word
    query = """
        SELECT MIN(rate) FROM word WHERE dictionary = ?;
    """
    cursor.execute(query, (dictionary_id,))
    result = cursor.fetchone()
    # Закрываем соединение
    conn.close()

    return result[0]

def count_word(dictionary_id:int,rate) -> int:
    """
    Получаем количество слов указаного рейтинг для  указанного ID словаря
    """
    # Подключение к базе данных
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # Получаем все записи из таблицы word
    query = """
        SELECT COUNT(*) FROM word WHERE dictionary = ? AND  rate = ?;
    """
    cursor.execute(query, (dictionary_id,rate,))
    result = cursor.fetchone()
    # Закрываем соединение
    conn.close()

    return result[0]



#print(word_for_practic(1, 0) )
#print(list_dictionary())
#print(min_rate(1))