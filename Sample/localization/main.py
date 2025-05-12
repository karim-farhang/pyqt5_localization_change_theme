import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QVBoxLayout, QWidget
from translator import Translator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translation Example")

        self.translator = Translator()

        # Widgets
        self.label = QLabel()
        self.language_combo = QComboBox()
        self.language_combo.addItems(["en", "fa", "ar"])
        self.language_combo.currentTextChanged.connect(self.change_language)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.language_combo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Bind text to translator
        self.translator.bind(self.label, "greeting")
        self.translator.bind(self.language_combo, "language", "setToolTip")  # Just for demo tooltip

    def change_language(self, lang_code):
        self.translator.set_language(lang_code)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
