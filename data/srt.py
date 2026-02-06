import re
import sqlite3
import os
from trip.d_1 import d_1


# запуск скрипта
# python data\srt.py

def read_text_auto_encoding(path):
    """
    Пытается открыть файл в нескольких популярных кодировках
    """
    encodings = ["utf-8", "utf-8-sig", "cp1251", "latin-1"]

    for enc in encodings:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError(f"Не удалось определить кодировку файла: {path}")


def parse_srt(path):
    content = read_text_auto_encoding(path)

    blocks = re.split(r"\n\s*\n", content.strip())
    lines = []

    for block in blocks:
        parts = block.splitlines()

        if len(parts) >= 3:
            text = " ".join(parts[2:]).strip()
            lines.append(text)

    return lines


def build_pairs(en_srt, ru_srt):
    en_lines = parse_srt(en_srt)
    ru_lines = parse_srt(ru_srt)

    if len(en_lines) != len(ru_lines):
        raise ValueError(
            f"Количество реплик не совпадает: EN={len(en_lines)}, RU={len(ru_lines)}"
        )

    return [(en, "", ru) for en, ru in zip(en_lines, ru_lines)]



en_file = "data\Zootopia.srt"
ru_file = "data\Zootopia_ru.srt"

words = build_pairs(en_file, ru_file)

#print(data)

dictionary = 2

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
