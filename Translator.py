from deep_translator import GoogleTranslator
import os

def translates(text, lang):
    translator = GoogleTranslator(source='english', target=lang)

    # with open('temp/temp.txt', 'w', encoding='utf-8') as f:
    #     f.write(translator.translate(text))
    # with open('temp/temp.txt', 'r', encoding='utf-8') as f:
    #     txt = f.read()
    # os.remove('temp/temp.txt')
    txt = translator.translate(text)
    return txt