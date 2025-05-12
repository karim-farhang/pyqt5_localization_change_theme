import json

# /home/karim/Desktop/Workspaces/pyqt_test/localization/translations.json
class Translator:
    def __init__(self, path='/home/karim/Desktop/Workspaces/pyqt_test/localization/translations.json'):
        with open(path, 'r', encoding='utf-8') as f:
            self.translations = json.load(f)
        self.current_lang = 'en'
        self._bindings = []

    def translate(self, key):
        return self.translations.get(self.current_lang, {}).get(key, key)

    def set_language(self, lang):
        if lang in self.translations:
            self.current_lang = lang
            self.update_all_widgets()

    def bind(self, widget, key, method='setText'):
        self._bindings.append((widget, key, method))
        getattr(widget, method)(self.translate(key))

    def update_all_widgets(self):
        for widget, key, method in self._bindings:
            getattr(widget, method)(self.translate(key))
