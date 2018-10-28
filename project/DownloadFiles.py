import requests
import re
from bs4 import BeautifulSoup
import os


def Standart(date):
    date = date.split(',')[0]
    date = date.split()
    if len(date) == 2:
        year = 2018
    else:
        year = date[2]
    months = {'января':'01', 'февраля':'02', 'марта':'03', 'апреля':'04', 'мая':'05', 'июня':'06', 'июля':'07', 'августа':'08', 'сентября':'09', 'октября':'10', 'ноября':'11', 'декабря':'12'}
    return '%s.%s.%s' % (date[0], months[date[1]], year)

def Year(raw_text):
    lines = raw_text.split('\n')
    x = lines[2].split()
    year = x[1].split('.')[2]
    month = (x[1].split('.')[1])
    return year, month

def BasicInfo(file_text, url):
    soup = BeautifulSoup(file_text, 'html5lib')
    header = soup.find(property="og:title").get('content')
    topic = soup.select('.date-catalog .catalog')[0].get_text()
    date = soup.select('.lcol .date')[0].get_text()
    s1 = '@au Noname\n'
    s2 = '@ti %s\n'% (header)
    s3 = '@da %s\n' % Standart(date)
    s4 = '@topic %s\n' % topic
    s5 = '@url %s\n' % url
    return (s1 + s2 + s3 + s4 + s5)


def PlainText(file_text):
    soup = BeautifulSoup(file_text, 'html5lib')
    image = soup.select('.newsarticle-img')
    if not image:
        image = ''
    else:
        image = image[0].get_text()
    summ = soup.select('.newsarticle-summary')[0].get_text()
    text = soup.select('.newsarticle-content')[0].get_text()
    return(image + '\n' + summ + '\n' + text)


def MakeTable(file_text, path, url, raw_text):
    soup = BeautifulSoup(file_text, 'html5lib')
    header = soup.find(property="og:title").get('content')
    created = Standart(soup.select('.lcol .date')[0].get_text())
    sphere = soup.select('.date-catalog .catalog')[0].get_text()
    year, m = Year(raw_text)
    s = [path, 'Noname', header, created, sphere, 'нейтральный', "н-возраст", "н-уровень", "районная", url, 'Ивановская газета', year, "газета", "Россия", 'Ивановкая область', "ru"]
    table.append(s)


def Downloader(name):
    print(name)
    result = requests.get(name)
    filetext = result.text
    if 'Error 404' in filetext:
        return False, False
    text = PlainText(filetext)
    text = BasicInfo(filetext, name) + text
    return text, filetext


def DownloadFrom():
    link = 'http://ivgazeta.ru/read/'
    for num in range(20, 4000):
        raw_text, file_text = Downloader(link + str(num))
        if raw_text:
            year, month = Year(raw_text)
            if not os.path.exists(DIR + '/' + DIR1 + '/' + year + '/' + month):
                os.makedirs(DIR + '/' + DIR1 + '/' + year + '/' + month)
            file = open(DIR + '/' + DIR1 + '/' + year + '/' + month + '/' + ('статья' + str(num) + '.txt'), 'w', encoding='utf-8')
            file.write(raw_text)
            file.close()
            MakeTable(file_text, DIR + '/' + DIR1 + '/' + year + '/' + month + '/' + ('статья' + str(num) + '.txt'), link + str(num), raw_text)


def CreateDirs():
    os.mkdir(DIR)
    os.mkdir(DIR + '/html')


def CreateTable():
    table = [['path', 'author', 'sex', 'birthday', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher', 'publ_year', 'medium', 'country', 'region', 'language']]
    return table

DIR = 'газета'
DIR1 = 'html'
table = CreateTable()
DownloadFrom()
with open(DIR + '/' + 'metadata.csv', 'w', encoding='utf-8') as file:
    for i in table:
        file.write('\t'.join(i) + '\n')


