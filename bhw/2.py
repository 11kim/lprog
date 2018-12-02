def stats():
    file = open('data.txt', 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    alts1 = {'ластик': set(), 'стирка': set(), 'резинка': set(), 'стёрка': set(), 'стиралка': set(), 'стирачка': set(), 'другое': set()}
    alts2 = {'ластик': set(), 'стирка': set(), 'резинка': set(), 'стёрка': set(), 'стиралка': set(), 'стирачка': set(), 'другое': set()}
    for line in data:
        if line == '':
            break
        line = line.rstrip()
        line = line.split(';')
        alts1[line[2]].add(line[0])
        alts2[line[2]].add(line[1])
    s = 'Распределение по городам\n'
    for i in alts1:
        s += i + ': ' + ', '.join(list(alts1[i])) + '\n'
    s += 'Распределение по возрасту\n'
    for i in alts2:
        s += i + ': ' + ', '.join(list(alts2[i])) + '\n'
    print(s)

stats()