import requests
from bs4 import BeautifulSoup


def create_url():
    url = 'https://context.reverso.net/translation/'
    language = input(
        'Type "en" if you want to translate from French into English, or "fr" if you want to translate from '
        'English into French:')
    word = input('Type the word you want to translate:')
    print('You chose', language, 'as the language to translate', word, 'to.')
    if language == 'fr':
        url += 'english-french/'
        language = 'French'
    else:
        url += 'french-english/'
        language = 'English'
    url += word
    print(url)
    return url, language


def make_get_request(search_url):
    r = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})
    print(r.status_code, 'OK\n')
    return r


def print_translations(web_page, language):
    translations = [word.text.strip() for word in web_page.find_all('a', class_='translation')[1:6]]
    print(language, 'Translations:')
    for word in translations:
        print(word)
    print("")


def print_examples(web_page, language):
    start_index = 33 if language == 'English' else 34
    examples = [sentence.text.strip() for sentence
                in web_page.find_all('span', class_='text')[start_index:start_index+10]]
    src_examples = examples[::2]
    trg_examples = examples[1::2]

    print(language, 'Examples:')
    for i in range(len(src_examples)):
        print(src_examples[i], '\b:')
        print(trg_examples[i], '\n')


def main():
    url, language = create_url()
    r = make_get_request(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    print('Context examples:\n')
    print_translations(soup, language)
    print_examples(soup, language)


main()
