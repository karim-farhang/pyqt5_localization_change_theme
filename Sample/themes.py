from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont

def apply_theme(app, theme='light'):
    if theme == 'dark':
        app.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #f0f0f0;
                font-size: 15px;
            }
            QPushButton, QComboBox {
                background-color: #444444;
                color: #f0f0f0;
                font-size: 15px;
            }
        """)
    else:
        app.setStyleSheet("""
            QWidget {
                font-size: 15px;
            }
            QPushButton, QComboBox {
                font-size: 15px;
            }
        """)

def apply_font(app, font_name='Arial', font_size=10):
    font = QFont(font_name, font_size)
    app.setFont(font)
