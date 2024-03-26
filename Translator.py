from deep_translator import GoogleTranslator
import os

def translates(text, lang):
    translator = GoogleTranslator(source='english', target=lang)
    txt = translator.translate(text)
    return txt