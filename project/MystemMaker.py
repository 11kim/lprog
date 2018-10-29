import os
import sys
import re


DIR = 'газета/plain'
for path, dirs, files in os.walk(DIR):
    for file in files:
        path1 = path.replace('plain', 'mystem-plain')
        path2 = path.replace('plain', 'mystem-xml')
        if not os.path.exists(path1):
            os.makedirs(path1)
            os.makedirs(path2)
        file2 = file.replace('txt', 'xml')
        os.system('mystem' + ' ' + (path + '/' + file) + ' ' + (path1 + '/' +  file) + ' -c -l -i -d --eng-gr -g')
        os.system('mystem' + ' ' + (path + '/' + file) + ' ' + (path2 + '/' + file2) + ' -c -l -i -d --eng-gr -g --format xml')









