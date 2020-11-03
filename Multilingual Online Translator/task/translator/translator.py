import requests
from bs4 import BeautifulSoup


def create_url():
    url = 'https://context.reverso.net/translation/'
    print("Hello, welcome to the translator. Translator supports:\n"
          "1. Arabic\n"
          "2. German\n"
          "3. English\n"
          "4. Spanish\n"
          "5. French\n"
          "6. Hebrew\n"
          "7. Japanese\n"
          "8. Dutch\n"
          "9. Polish\n"
          "10. Portuguese\n"
          "11. Romanian\n"
          "12. Russian\n"
          "13. Turkish\n")
    src_language = get_language_string(input('Type the number of your language:'))
    url += src_language.lower()
    trg_language = get_language_string(input('Type the number of language you want to translate to:'))
    url += "-" + trg_language.lower() + "/"
    word = input('Type the word you want to translate:')
    url += word
    print(url)
    return url, trg_language


def get_language_string(language):
    languages = {"1": "Arabic", "2": "German", "3": "English", "4": "Spanish", "5": "French",
                 "6": "Hebrew", "7": "Japanese", "8": "Dutch", "9": "Polish", "10": "Portuguese",
                 "11": "Romanian", "12": "Russian", "13": "Turkish"}
    return languages.get(language)


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
                in web_page.find_all('span', class_='text')[start_index:start_index + 10]]
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
