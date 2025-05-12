import json

class Translator:
    def __init__(self, json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            self.translations = json.load(f)
        self.current_lang = 'en'

    def set_language(self, lang_code):
        if lang_code in self.translations:
            self.current_lang = lang_code

    def translate(self, key):
        return self.translations.get(self.current_lang, {}).get(key, key)
