import os
import requests

# -- Dev Notes --
# Add correct documentation 
# Create class
# Ensure request and fiel save are seperate processes


r = requests.get('https://www.wordgamedictionary.com/sowpods/download/sowpods.txt')
# print(r.headers)
# print(r.headers['content-type'])
# print(r.encoding)
# word_list = r.text.splitlines()
# word_list = word_list[6:]

with open(os.path.join('.', 'words.txt'), 'wb') as fd:
    fd.write(r.content)