import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QVBoxLayout, QWidget, QComboBox, QFormLayout
)
from PyQt5.QtCore import Qt
from translator import Translator
from themes import apply_theme, apply_font
from date_utils import get_gregorian_date, get_jalali_date, get_hijri_date
from settings_manager import SettingsManager

class MainWindow(QMainWindow):


    def __init__(self, settings_manager):
        super().__init__()
        self.settings_manager = settings_manager
        self.translator = Translator()
        self.init_ui()
        self.settings_manager.setting_changed.connect(self.on_setting_changed)


    def init_ui(self):
        self.setWindowTitle("Multi-language App")
        self.setMinimumSize(500, 350)  # Set a medium window size

        self.label = QLabel()
        self.label.setMinimumHeight(40)
        self.label.setStyleSheet("font-size: 18px;")
        self.translator.bind(self.label, "greeting")

        # Add labels for combos
        self.theme_label = QLabel()
        self.theme_label.setStyleSheet("font-size: 15px;")
        self.translator.bind(self.theme_label, "theme")
        self.theme_combo = QComboBox()
        self.theme_combo.setMinimumHeight(30)
        self.theme_combo.setStyleSheet("font-size: 15px;")
        self.theme_combo.addItems(["light", "dark"])
        self.theme_combo.currentTextChanged.connect(self.change_theme)

        self.font_label = QLabel()
        self.font_label.setStyleSheet("font-size: 15px;")
        self.translator.bind(self.font_label, "font")
        self.font_combo = QComboBox()
        self.font_combo.setMinimumHeight(30)
        self.font_combo.setStyleSheet("font-size: 15px;")
        self.font_combo.addItems(["Arial", "Times New Roman", "Courier New"])
        self.font_combo.currentTextChanged.connect(self.change_font)

        self.language_label = QLabel()
        self.language_label.setStyleSheet("font-size: 15px;")
        self.translator.bind(self.language_label, "language")
        self.language_combo = QComboBox()
        self.language_combo.setMinimumHeight(30)
        self.language_combo.setStyleSheet("font-size: 15px;")
        self.language_combo.addItems(["en", "fa", "ar"])
        self.language_combo.currentTextChanged.connect(self.change_language)

        self.date_label = QLabel()
        self.date_label.setStyleSheet("font-size: 16px;")
        self.update_date()

        # Use QFormLayout for better alignment
        form_layout = QFormLayout()
        form_layout.setSpacing(18)
        form_layout.addRow(self.label)
        form_layout.addRow(self.theme_label, self.theme_combo)
        form_layout.addRow(self.font_label, self.font_combo)
        form_layout.addRow(self.language_label, self.language_combo)
        form_layout.addRow(self.date_label)

        container = QWidget()
        container.setLayout(form_layout)
        self.setCentralWidget(container)

        # Set initial layout direction
        self.update_layout_direction(self.translator.current_lang)

    def change_theme(self, theme):
        self.settings_manager.set_value("theme", theme)

    def change_font(self, font_name):
        self.settings_manager.set_value("font", font_name)

    def change_language(self, lang):
        self.settings_manager.set_value("language", lang)

    def on_setting_changed(self, key, value):
        if key == "theme":
            apply_theme(app, value)
        elif key == "font":
            apply_font(app, value)
        elif key == "language":
            self.translator.set_language(value)
            self.update_date()
            self.update_layout_direction(value)
            # Update combo labels to reflect new language
            self.translator.update_all_widgets()

    def update_date(self):
        lang = self.translator.current_lang
        if lang == 'fa':
            date = get_jalali_date()
        elif lang == 'ar':
            date = get_hijri_date()
        else:
            date = get_gregorian_date()
        self.date_label.setText(f"{self.translator.translate('date')}: {date}")

    def update_layout_direction(self, lang):
        if lang in ['fa', 'ar']:
            self.centralWidget().setLayoutDirection(Qt.RightToLeft)
        else:
            self.centralWidget().setLayoutDirection(Qt.LeftToRight)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    settings_manager = SettingsManager()
    apply_theme(app, settings_manager.get_value("theme", "light"))
    apply_font(app, settings_manager.get_value("font", "Arial"), 14)  # Increase default font size
    window = MainWindow(settings_manager)
    window.show()
    sys.exit(app.exec_())