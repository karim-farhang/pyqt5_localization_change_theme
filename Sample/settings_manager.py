from PyQt5.QtCore import QObject, pyqtSignal, QSettings

class SettingsManager(QObject):
    setting_changed = pyqtSignal(str, object)

    def __init__(self):
        super().__init__()
        self.settings = QSettings("MyCompany", "MyApp")

    def set_value(self, key, value):
        self.settings.setValue(key, value)
        self.setting_changed.emit(key, value)

    def get_value(self, key, default=None):
        return self.settings.value(key, default)