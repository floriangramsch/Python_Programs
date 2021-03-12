#!/usr/bin/env python

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QShortcut
import sys
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_CODES_TO_LANGUAGES
import random


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Translator")

        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.v_box = QVBoxLayout(self.centralwidget)

        # SET LANGUAGES
        self.languages = [
            [QtWidgets.QLabel(self), QtWidgets.QLineEdit(self)],
            [QtWidgets.QLabel(self), QtWidgets.QLineEdit(self)],
            [QtWidgets.QLabel(self), QtWidgets.QLineEdit(self)],
            [QtWidgets.QLabel(self), QtWidgets.QLineEdit(self)],
            [QtWidgets.QLabel(self), QtWidgets.QLineEdit(self)]
        ]

        self.languages[0][0].setText("German")
        self.languages[1][0].setText("English")
        self.languages[2][0].setText("Norwegian")
        self.languages[3][0].setText("French")
        self.languages[4][0].setText("Random")

        # BUTTON
        self.translate_button = QtWidgets.QPushButton(self)
        self.translate_button.pressed.connect(self.init_translate)
        self.translate_button.setText("Translate")
        self.shortcut_translate = QShortcut(QtGui.QKeySequence('Return'), self)
        self.shortcut_translate.activated.connect(self.init_translate)

        self.reset_button = QtWidgets.QPushButton(self)
        self.reset_button.pressed.connect(self.reset)
        self.reset_button.setText("Reset")
        self.shortcut_reset = QShortcut(QtGui.QKeySequence('Enter'), self)
        self.shortcut_reset.activated.connect(self.reset)

        # HORIZONTAL LAYOUT
        self.h_box_german = QHBoxLayout()
        self.h_box_german.addWidget(self.languages[0][0])
        self.h_box_german.addWidget(self.languages[0][1])

        self.h_box_english = QHBoxLayout()
        self.h_box_english.addWidget(self.languages[1][0])
        self.h_box_english.addWidget(self.languages[1][1])

        self.h_box_norwegian = QHBoxLayout()
        self.h_box_norwegian.addWidget(self.languages[2][0])
        self.h_box_norwegian.addWidget(self.languages[2][1])

        self.h_box_french = QHBoxLayout()
        self.h_box_french.addWidget(self.languages[3][0])
        self.h_box_french.addWidget(self.languages[3][1])
        
        self.h_box_random = QHBoxLayout()
        self.h_box_random.addWidget(self.languages[4][0])
        self.h_box_random.addWidget(self.languages[4][1])

        self.h_box_buttons = QHBoxLayout()
        self.h_box_buttons.addWidget(self.translate_button)
        self.h_box_buttons.addWidget(self.reset_button)

        # ADD LAYOUTS
        self.v_box.addLayout(self.h_box_german)
        self.v_box.addLayout(self.h_box_english)
        self.v_box.addLayout(self.h_box_norwegian)
        self.v_box.addLayout(self.h_box_french)
        self.v_box.addLayout(self.h_box_random)
        self.v_box.addLayout(self.h_box_buttons)

        self.setCentralWidget(self.centralwidget)


    def reset(self):
        for i in self.languages:
            i[1].setText("")
        self.languages[len(self.languages)-1][0].setText("Random")

    def init_translate(self):
        for i in self.languages:
            if i[1].text() != "":
                self.translate(i[0].text(), i[1].text())
                return

    def translate(self, language, to_translate):
        random_language = random.choice(list(GOOGLE_CODES_TO_LANGUAGES.values()))
        for j in self.languages:
            if j[0].text() != language:
                if j[0].text() == "Random":
                    translator = GoogleTranslator(source=language.lower(), target=random_language)
                    j[1].setText(translator.translate(to_translate))
                    j[0].setText(random_language)
                    continue
                translator = GoogleTranslator(source=language.lower(), target=j[0].text().lower())
                j[1].setText(translator.translate(to_translate))


def main():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

if "__main__" == __name__:
    main()
