import os
import re

'''
dir = 'stexts'
for filename in os.listdir(dir):
    fin = open(dir + '/' + filename, 'r')
    f = fin.read()
    fin.close()
    filename = re.sub('[\d]+ \- ', '', filename)
    print(filename)
    fout = open(dir + '/' + filename, 'w', encoding='utf-8')
    fout.write(f)
    fout.close()
'''

s = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title> {name} </title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
</head>
<body>
    <div><PRE>{text}</PRE></div>
</body>
</html>'''

dir = 'notexts'
dir2 = 'templates'
for filename in os.listdir(dir):
    fin = open(dir + '/' + filename, 'r')
    f = fin.read()
    fin.close()
    name = re.sub('\.txt', '', filename)
    filename = re.sub('\.txt', '.html', filename)
    s1 = s.format(name=name.upper(), text=f)
    fout = open(dir2 + '/' + filename, 'w')
    fout.write(s1)
    fout.close()