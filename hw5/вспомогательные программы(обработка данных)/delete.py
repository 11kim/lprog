import sqlite3
import os
import re

'''conn = sqlite3.connect('corpus.db')
c = conn.cursor()

c.execute("DELETE FROM data")
c.execute("DELETE FROM sqlite_sequence")
conn.commit()

c.execute("ALTER TABLE data ADD COLUMN name TEXT")
conn.commit()'''
DIR = 'texts2'

links = open('links.txt', 'w', encoding='utf-8')
names = open('names.txt', 'w', encoding='utf-8')
for path, dirs, files in os.walk(DIR):
    for filename in files:
        print(filename)
        fin = open(path + '/' + filename, 'r', encoding='UTF-8')
        #lines = fin.readlines()
        text = fin.read()
        fin.close()
        s = re.findall('@url (.+)\n', text)
        link = s[0]
        s = re.findall('@ti (.+)\n', text)
        name = s[0]
        links.write(filename + ' ' + link + '\n')
        names.write(filename + ' ' + name + '\n')
links.close()
names.close()
