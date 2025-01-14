import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from pathlib import Path
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        uic.loadUi(Path('UI.ui'), self)
        self.setFixedSize(500, 500)
        self.color = QColor('yellow')
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(self.color)
        radius = randint(0, 100)
        qp.drawEllipse(QPoint(250, 250), radius, radius)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
