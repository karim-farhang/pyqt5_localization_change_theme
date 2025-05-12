import json

class Translator:
    def __init__(self, json_path='/home/karim/Desktop/Workspaces/pyqt_test/Sample/translations.json'):
        with open(json_path, 'r', encoding='utf-8') as f:
            self.translations = json.load(f)
        self.current_lang = 'en'
        self._bound_widgets = []

    def set_language(self, lang_code):
        if lang_code in self.translations:
            self.current_lang = lang_code
            self.update_all_widgets()

    def translate(self, key):
        return self.translations.get(self.current_lang, {}).get(key, key)

    def bind(self, widget, key, attr="setText"):
        self._bound_widgets.append((widget, key, attr))
        getattr(widget, attr)(self.translate(key))

    def update_all_widgets(self):
        for widget, key, attr in self._bound_widgets:
            getattr(widget, attr)(self.translate(key))