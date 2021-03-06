from flask import Flask, request
from flask import render_template
import json


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('questionlist.html')

@app.route('/info', methods=['post'])
def info():
    place = request.form['place'].lower()
    age = request.form['age']
    if not age.isdigit():
        age = 0
    ans = request.form['eraser']
    file = open('data.txt', 'a', encoding='utf-8')
    s = place + ';' + age + ';' + ans + '\n'
    file.write(s)
    file.close()
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    data[ans].append({'place':place, 'age':age})
    file = open('data.json', 'w', encoding='utf-8')
    json.dump(data, file, sort_keys=True, indent=2, ensure_ascii=False)
    return '<p><a href="http://127.0.0.1:5000/"> Вернуться на главную страницу </a><br><a href="http://127.0.0.1:5000/stats"> Посмотреть статистику </a></p>'


@app.route('/json')
def bprint():
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    s = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)
    file.close()
    return s

@app.route('/stats')
def stats():
    file = open('data.txt', 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    alts1 = {'ластик': set(), 'стирка': set(), 'резинка': set(), 'стёрка': set(), 'стиралка': set(),
                 'стирачка': set(), 'другое': set()}
    alts2 = {'ластик': set(), 'стирка': set(), 'резинка': set(), 'стёрка': set(), 'стиралка': set(),
                 'стирачка': set(), 'другое': set()}
    for line in data:
        if line == '':
            break
        line = line.rstrip()
        line = line.split(';')
        alts1[line[2]].add(line[0])
        alts2[line[2]].add(line[1])
    s = 'Распределение по городам<br>'
    for i in alts1:
        s += i + ': ' + ', '.join(list(alts1[i])) + '<br>'
    s += 'Распределение по возрасту<br>'
    for i in alts2:
        s += i + ': ' + ', '.join(list(alts2[i])) + '<br>'
    return s

app.run(debug='True')