from bottle import route, run, template, request, view, debug, redirect
from db.select import list_dictionary, word_for_practic, min_rate, count_word
from db.update import update_rate
import random
from voice import voice


def server_bottle():
    @route('/')
    @view('html_template/template_choise') 
    def index():
        """ Индексная страница - СТАРТ 
        выбираем словари для обучения
        """
        data = list_dictionary()
        word = "sffsgf sdg "    
        return dict(data=data)


    @route(f'/dic/<id_dic:int>/<rate:int>')
    @view('html_template/template_word') 
    def word(id_dic, rate=None):
        rg = int(request.query.rg or 0)
        er = int(request.query.er or 0)
        erall = int(request.query.erall or 0)

        if er != 0: # ID слова в котором ошиблись 
            # понижаем рейтинг слова
            erall+=1
            update_rate(er, rate-1)

        if rg != 0: # ID слова в которое ответили правильно
            # повышаем рейтинг слова
            update_rate(rg, rate+1)

        if erall >= 10: # количестов ошибок за урок
            # начинаем урок заново
            redirect(f'/')

        word=word_for_practic(id_dic, rate)
        er_add = er+1
        counter = count_word(id_dic, rate)
        if counter == 0:
            # если слова закончилсь
            # начинаем урок заново
            redirect(f'/')
        voice(word[1], word[3])
        return dict(dic=id_dic,
                    word=word,
                    rate=rate,
                    er=er,
                    er_add=er_add,
                    erall=erall,
                    counter=counter
                    ) 
    
    
    # определяем минимальный rate
    @route(f'/dic/<id_dic:int>')
    @view('html_template/template_start') 
    def word(id_dic):
        rate = min_rate(id_dic)
        return dict(data=(id_dic,rate,))
    







    debug(True)
    run(host='localhost', port=8080, debug=True, reloader=True)