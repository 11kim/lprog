from flask import Flask, request
from flask import render_template
from pymystem3 import Mystem
import re
import sqlite3
import os.path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/info', methods=['post'])
def info():
    word = request.form['word'].lower()
    if word == '':
        return 'Задан пустой поисковый запрос'
    if not (re.fullmatch('[а-яё ]+', word) or re.fullmatch('[а-яё]+\-[а-яё]+', word)):
        return 'Некорректный ввод <br><a href="./">Домой!</a>'
    m = Mystem()
    lexword = m.lemmatize(word)[0]



    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "songs.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    x = '"% ' + lexword + ' %"'
    x1 = '"' + lexword + ' %"'
    x2 = '"% ' + lexword + '"'
    c.execute('SELECT id, name, author, source FROM TEXTS WHERE lextext LIKE {x} OR lextext LIKE {x1} OR lextext LIKE {x2}'.format(x=x, x1=x1, x2=x2))


    res = []
    for i in (c.fetchall()):
        id = i[0]
        name = i[1]
        print(name)
        author = i[2]
        source = i[3]
        if not source:
            source = 'Концерты'
        if author == 'дуэт':
            author = 'точно не ясно, но точно кто-то из них, а может, оба'
        res.append(("song/" + str(id), name, author, source))


    conn.commit()
    conn.close()
    if not res:
        return 'Таких слов не обнаружено <br><a href="./">Домой!</a>'
    return render_template('answer.html', res=res)


@app.route('/song/<id>')
def song(id):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "songs.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT name FROM TEXTS WHERE id={}'.format(id))
    name = c.fetchone()[0]
    return render_template(name + '.html')



if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)