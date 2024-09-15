import requests
from bs4 import BeautifulSoup

class Translator:

    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
        self.soup = ''
        # self.lang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
        # self.word = input('Type the word you want to translate:\n')

    def requestSoup(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        if self.lang == 'fr':
            url = 'https://context.reverso.net/translation/english-french/' + self.word
        elif self.lang == 'en':
            url = 'https://context.reverso.net/translation/french-english/' + self.word
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if page.status_code == 200:
            print('200 OK\nTranslations')

        self.soup = soup

    def wordList(self):
        wordList = []

        for x in self.soup.find_all('span', {'class': 'display-term'}):
            wordList.append(x.text)
        print(wordList)

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

        for en, fr in zip(englishList, frenchList):
            if self.lang == 'en':
                finalList.append(fr)
                finalList.append(en)
            elif self.lang == 'fr':
                finalList.append(en)
                finalList.append(fr)
        print(finalList)

    def __str__(self):
        return f'You chose "{self.lang}" as the language to translate "{self.word}" to.'
        

userLang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
userWord = input('Type the word you want to translate:\n')
user = Translator(userWord, userLang)

print(user)
user.requestSoup()
user.wordList()
user.sentenceList()
