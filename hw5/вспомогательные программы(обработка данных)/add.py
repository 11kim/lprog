import sqlite3
import os
import re


conn = sqlite3.connect('corpus.db')
c = conn.cursor()

DIR = 'texts'
DIR2 = 'lemmtexts'

links_f = open('links.txt', 'r', encoding='utf-8')
linkslist = links_f.readlines()
links_f.close()
links = {}
for i in linkslist:
    filename, link = i.rstrip().split()
    links[filename] = link

names_f = open('names.txt', 'r', encoding='utf-8')
namelist = names_f.readlines()
names_f.close()
names = {}
for i in namelist:
    s = re.findall('(статья[0-9]+.txt) (.+)', i.rstrip())[0]
    filename, name = s[0], s[1]
    names[filename] = name

c.execute("DELETE FROM data")
c.execute("DELETE FROM sqlite_sequence")
conn.commit()

for path, dirs, files in os.walk(DIR):
    path2 = path.replace('texts', 'lemmtexts')
    for filename in files:
        fin = open(path + '/' + filename, 'r', encoding='UTF-8')
        text = fin.read()
        fin.close()
        fin = open(path2 + '/' + filename, 'r', encoding='UTF-8')
        lemmtext = fin.read()
        fin.close()
        link = links[filename]
        name = names[filename]

        c.execute("INSERT INTO data (text, lemmtext, link, name) VALUES (?, ?, ?, ?)", (text, lemmtext, link, name))
        conn.commit()

conn.close()