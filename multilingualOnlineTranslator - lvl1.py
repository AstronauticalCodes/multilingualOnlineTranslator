class Translator:

    def __init__(self, word, lang):
        self.word = word
        self.lang = lang

    def __str__(self):
        return f'You chose "{self.lang}" as the language to translate "{self.word}" to.'

userLang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
userWord = input('Type the word you want to translate:\n')
user = Translator(userWord, userLang)
print(user)
