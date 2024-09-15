import requests
from bs4 import BeautifulSoup

class Translator:
    avoids = ['"', '»', '«']
    langDict = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew', 7: 'Japanese', 8: 'Dutch', 9: 'Polish', 10: 'Portuguese', 11: 'Romanian', 12: 'Russian', 13: 'Turkish'}
    langCodes = {1: 'ar', 2: 'de', 3: 'en', 4: 'es', 5: 'fr', 6: 'iw', 7: 'ja', 8: 'nl', 9: 'pl', 10: 'pt-PT', 11: 'ro', 12: 'ru', 13: 'tr'}

    def __init__(self):
        print('''Hello, welcome to the translator. Translator supports: \n1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese\n8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish''')
        self.sourceLang = int(input('Type the number of your language:\n'))
        self.targetLang = int(input('Type the number of language you want to translate to:\n'))
        self.word = input('Type the word you want to translate:\n')
        # self.lang = lang
        self.soup = ''
        self.targetLangList = []
        self.sourceLangList = []
        # self.lang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
        # self.word = input('Type the word you want to translate:\n')
        self.requestSoup()
        self.wordList()
        self.sentenceList()


    def requestSoup(self):
        headers = {'User-Agent': 'Mozilla/5.0'}

        url = f'https://context.reverso.net/translation/{self.langDict[self.sourceLang].lower()}-{self.langDict[self.targetLang].lower()}/' + self.word
        # print(url)

        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        if page.status_code == 200:
            print(f'200 OK\n\n{self.langDict[self.targetLang]} Translations:')

        self.soup = soup

    def wordList(self):

        for index, x in enumerate(self.soup.find_all('span', {'class': 'display-term'})):
            if index == 5:
                print(f'\n{self.langDict[self.targetLang]} Examples:')
                break
            else:
                wordList = []
                for char in x.text:
                    if char not in self.avoids:
                        wordList.append(char)
                print(''.join(wordList))


    def sentenceList(self):
        if self.sourceLang == 3:
            self.targetLangListMaker()
            self.sourceLangListMaker()
        else:
            self.sourceLangListMaker()
            self.targetLangListMaker()

        for index, langs in enumerate(zip(self.sourceLangList, self.targetLangList)):
            source, target = langs
            if index < 5:
                print(f'{source}:\n{target}')
                print()

        
    def sourceLangListMaker(self):
        if self.sourceLang != 3:
            for x in self.soup.find_all('span', {'class': 'text', 'lang': self.langCodes[self.sourceLang]}):
                self.sourceLangList.append(x.text.strip('\r\n          '))
        
        else:
            for y in self.soup.find_all('span', {'class': 'text'}):
                if self.word in y.text and y.text not in self.targetLangList:
                    self.sourceLangList.append(y.text.strip('\r\n          '))
                    
    def targetLangListMaker(self):
        if self.targetLang != 3:  
            for x in self.soup.find_all('span', {'class': 'text', 'lang': self.langCodes[self.targetLang]}):
                self.targetLangList.append(x.text.strip('\r\n          '))

        else:
            for y in self.soup.find_all('span', {'class': 'text'}):
                if y.find('a'):
                    self.targetLangList.append(y.text.strip('\r\n          '))

        # print(finalList)


# userLang = input('''Hello, welcome to the translator. Translator supports: \n1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese\n8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish''')
# userWord = input('Type the word you want to translate:\n')
# user = Translator(userWord, userLang)
#
# print(user)
# user.requestSoup()
# user.wordList()
# user.sentenceList()
Translator()
