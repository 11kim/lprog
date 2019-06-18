import sqlite3

conn = sqlite3.connect('songs.db')
c = conn.cursor()

lexword = 'злой'

x = '"%' + lexword + '%"'
print(x)
c.execute('SELECT text, name, author, source FROM TEXTS WHERE lextext LIKE {}'.format(x))

for i in (c.fetchall()):
    print(i[1])

conn.commit()


conn.close()