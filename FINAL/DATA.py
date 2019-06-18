import sqlite3
import os
import re
from pymystem3 import Mystem

def MakeItPlain(text):
    text = text.lower()
    text = re.sub('[,/.:;!?"]', '', text)
    text = re.sub('[a-z\d#|\+\(\)]', '', text)
    return text


def MakeItLex(plaintext):
    m = Mystem()
    lemmas = m.lemmatize(plaintext)
    return ''.join(lemmas)


conn = sqlite3.connect('songs.db')
c = conn.cursor()


dir = 'stexts'
for filename in os.listdir(dir):
    fin = open(dir + '/' + filename, 'r')
    text = fin.read()
    fin.close()
    author = 'дуэт'
    if ('Иващенко' in text) and ('Васильев' in text):
        author = 'А.И.Иващенко И Г.Л.Васильев'
    elif 'Иващенко' in text:
        author = 'А.И.Иващенко'
    elif 'Васильев' in text:
        author = 'Г.Л.Васильев'
    source = None
    name = re.sub('\.txt', '', filename)
    plaintext = MakeItPlain(text)
    lextext = MakeItLex(plaintext)
    if text:
        c.execute('INSERT INTO TEXTS (text, lextext, name, author, source) VALUES (?, ?, ?, ?, ?)', (text, lextext, name, author, source))
    print(filename)


dir = 'notexts'
for filename in os.listdir(dir):
    fin = open(dir + '/' + filename, 'r')
    text = fin.read()
    fin.close()
    author = 'дуэт'
    source = 'мюзикл Норд-Ост'
    name = re.sub('\.txt', '', filename)
    plaintext = MakeItPlain(text)
    lextext = MakeItLex(plaintext)
    c.execute('INSERT INTO TEXTS (text, lextext, name, author, source) VALUES (?, ?, ?, ?, ?)', (text, lextext, name, author, source))
    print(filename)



#c.execute('INSERT INTO TEXTS (text, lextext, name, author, source) VALUES (?, ?, ?, ?, ?)', (text, lextext, name, author, source))


#c.execute('DELETE FROM TEXTS')

#c.execute('DROP TABLE IF EXISTS TEXTS')
conn.commit()


conn.close()