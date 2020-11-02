import requests
from bs4 import BeautifulSoup

url = 'https://context.reverso.net/translation/'
language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from '
                 'English into French:')
word = input('Type the word you want to translate:')

print('You chose', language, 'as the language to translate', word, 'to.')

if language == 'fr':
    url += 'english-french/'
else:
    url += 'french-english/'
url += word

r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print(r.status_code, 'OK')
soup = BeautifulSoup(r.content, 'html.parser')


translations = [word.text.strip() for word in soup.find_all('a', class_='translation')[1:]]
examples = [sentence.text.strip() for sentence in soup.find_all('span', class_='text')[34:]]

print("Translations")
print(translations)
print(examples)