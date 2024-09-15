import requests
from bs4 import BeautifulSoup

class Translator:
    avoids = ['"', '»', '«']

    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
        self.soup = ''
        self.language = ''
        # self.lang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
        # self.word = input('Type the word you want to translate:\n')

    def requestSoup(self):
        headers = {'User-Agent': 'Mozilla/5.0'}

        if self.lang == 'fr':
            self.language = 'French'
            url = 'https://context.reverso.net/translation/english-french/' + self.word
        elif self.lang == 'en':
            self.language = 'English'
            url = 'https://context.reverso.net/translation/french-english/' + self.word

        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        if page.status_code == 200:
            print(f'200 OK\n\n{self.language} Translations:')

        self.soup = soup

    def wordList(self):

        for index, x in enumerate(self.soup.find_all('span', {'class': 'display-term'})):
            if index == 5:
                print(f'\n{self.language} Examples:')
                break
            else:
                wordList = []
                for char in x.text:
                    if char not in self.avoids:
                        wordList.append(char)
                print(''.join(wordList))


    def sentenceList(self):
        englishList = []
        frenchList = []
        finalList = []
        for x in self.soup.find_all('span', {'class': 'text', 'lang': 'fr'}):
            frenchList.append(x.text.strip('\r\n          '))

        for y in self.soup.find_all('span', {'class': 'text'}):
            if self.lang == 'en':
                if y.find('a'):
                    englishList.append(y.text.strip('\r\n          '))
            elif self.word in y.text and y.text not in frenchList:
                englishList.append(y.text.strip('\r\n          '))

        for index, langs in enumerate(zip(englishList, frenchList)):
            en, fr = langs
            if index < 5:
                if self.lang == 'en':
                    print(f'{fr}\n{en}')
                    # finalList.append(fr)
                    # finalList.append(en)
                elif self.lang == 'fr':
                    print(f'{en}\n{fr}')
                    # finalList.append(en)
                    # finalList.append(fr)
                print()
        # print(finalList)

    def __str__(self):
        return f'You chose "{self.lang}" as the language to translate "{self.word}" to.'


userLang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
userWord = input('Type the word you want to translate:\n')
user = Translator(userWord, userLang)

print(user)
user.requestSoup()
user.wordList()
user.sentenceList()
