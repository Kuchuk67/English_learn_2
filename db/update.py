import sqlite3

def update_dictionary(dictionary_id, new_name):
    """ Изменить значение словаря, 
    ID словаря который нужно изменить, новое название
    """
    # Подключение к БД
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # SQL-запрос на обновление
    update_sql = """
    UPDATE dictionary
    SET name = ?
    WHERE id = ?
    """
    # Выполнение запроса с параметрами
    cursor.execute(update_sql, (new_name, dictionary_id))
    # Сохраняем изменения
    conn.commit()
    conn.close()
    print(f"Название словаря с id={dictionary_id} успешно изменено на '{new_name}'")


def update_rate(id:int,new_rate:int):
    """
    Изменяет рейтинг слова
    """
    # Подключение к БД
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # SQL-запрос на обновление
    update_sql = """
    UPDATE word
    SET rate = ?
    WHERE id = ?
    """
    # Выполнение запроса с параметрами
    cursor.execute(update_sql, (new_rate, id))
    # Сохраняем изменения
    conn.commit()
    conn.close()
    print(f"Название словаря с id={id} успешно изменено на '{new_rate}'")

#update_dictionary(2,"Words for polite conversations")
#update_rate(43,0)

