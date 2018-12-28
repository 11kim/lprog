import sqlite3
import os


def find(askl, lemm):
    elem = askl[0]
    for i in range(len(lemm)):
        if lemm[i] == elem:
            #print(lemm[i:i+len(askl)], askl)
            if lemm[i:i+len(askl)] == askl:
                return i
    return 0



conn = sqlite3.connect('corpus.db')
c = conn.cursor()

ask = input()
fin = open('ask.txt', 'w', encoding='utf-8')
fin.write(ask)
fin.close()
os.system('mystem' + ' ' + 'ask.txt' + ' ' +  'ask' + ' -c -l -d --eng-gr -g')
fin = open('ask', 'r', encoding='utf-8')
ask = fin.read()
ask = ask.rstrip()


sq = "SELECT * FROM data WHERE lemmtext LIKE ?"
c.execute(sq, ['%' + ask + '%'])
conn.commit()
ans = c.fetchall()
for i in ans:
    id, text, lemmtext, link, name = i[0], i[1], i[2], i[3], i[4]
    lemm = lemmtext.split()
    askl = ask.split()
    #print(askl)
    ind = find(askl, lemm)
    print(ind)
    textl = text.split()
    ind0 = max(0, ind - 10)
    ind1 = min(len(textl) - 1, ind + len(askl) + 10)
    req = (textl[ind0:ind1])
    req = ' '.join(req)
    print(name, link)
    print(req)


