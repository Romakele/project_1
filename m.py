import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 75)
        self.setWindowTitle('Программа')

        self.first_value = QLineEdit(self)
        self.first_value.resize(150, 30)
        self.first_value.move(20, 30)

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(30, 30)
        self.trick_button.move(180, 30)
        self.trick_button.clicked.connect(self.calc)

        self.second_value = QLineEdit(self)
        self.second_value.resize(150, 30)
        self.second_value.move(220, 30)

    def calc(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == '__mane__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())