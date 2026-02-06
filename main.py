from db.create_db import create_db
from server import server_bottle
import sys
from bottle import route, run, template, request, view, debug

list_words = []

try:
    command = sys.argv[1]
except IndexError:
    print("""
        main.py 1 - Создать БД
        main.py 2 - Ввод новых слов
        main.py 3 - запустить HTML-сервер
        main.py 9 - Удаление данных
        """)
    sys.exit()

if command=='1':
    create_db()

if command=='3':
    server_bottle()

'''

@route('/')
def index():
    """ Индексная страница - СТАРТ 
    выбираем словари для обучения
    """
            
    return f'<a href="/d1">Выбрать словарь d1</a><br><a href="/d2">Выбрать словарь d2</a>'


debug(True)
run(host='localhost', port=8080, debug=True, reloader=True)'''