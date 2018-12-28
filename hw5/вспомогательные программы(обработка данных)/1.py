import os


DIR = 'texts'
DIR2 = 'lemmtexts'

#links = open('links.txt', 'w', encoding='utf-8')
#names = open('names.txt', 'w', encoding='utf-8')

for path, dirs, files in os.walk(DIR):
    for filename in files:
        print(filename)
        fin = open(path + '/' + filename, 'r', encoding='UTF-8')
        lines = fin.readlines()
        fin.close()
        while lines[0].startswith('@'):
            if lines[0].startswith('@url'): 
                link = lines[0].split()[1]
                #links.writelines(filename + ' ' + link + '\n')
                lines.pop(0)
            elif lines[0].startswith('@ti'):
                name = lines[0].split()[1]
                #names.writelines(filename + ' ' + name + '\n')
                lines.pop(0)
            else:
                lines.pop(0)
        text = ''.join(lines)
        text = text.replace('\n', ' ')
        #print(text)
        fout = open(path + '/' + filename, 'w', encoding='UTF-8')
        fout.write(text)
        fout.close()
        path1 = path.replace('texts', 'lemmtexts')
        os.system('mystem' + ' ' + (path + '/' + filename) + ' ' + (path1 + '/' +  filename) + ' -c -l -d --eng-gr -g')

#links.close()
#names.close()