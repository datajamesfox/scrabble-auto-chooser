import os
import requests

r = requests.get('https://www.wordgamedictionary.com/sowpods/download/sowpods.txt')
print(r.headers)
print(r.headers['content-type'])
print(r.encoding)
word_list = r.text.splitlines()

print(word_list)

with open(os.path.join('.', 'words.txt'), 'wb') as fd:
    fd.write(r.content)