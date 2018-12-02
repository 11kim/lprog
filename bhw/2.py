import json

file = open('data.json', 'r', encoding='utf-8')
s = json.load(file)
print(s)
file.close()
file = open('data.json', 'w', encoding='utf-8')
json.dump(s, file, indent=2, ensure_ascii=False)