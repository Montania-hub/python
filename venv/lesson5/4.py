from googletrans import Translator
translator = Translator()
with open('41.txt', 'r') as f1:
    with open('42.txt', 'w', encoding = 'utf-8') as f2:
        f2.write(translator.translate(f1, src='en', dest='ru'))



