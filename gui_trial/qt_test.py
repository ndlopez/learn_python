# display hello world on window

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

#print version of Pyside
# print(PySide6.__version__)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ["Hallo arbeit","Hello work","ハローワーク","Hello QtWidget"]
        self.button = QtWidgets.QPushButton("Click me")
        self.text = QtWidgets.QLabel("Hallo work",alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
        app= QtWidgets.QApplication([])
        widget = MyWidget()
        widget.resize(400,300)
        widget.show()
        sys.exit(app.exec())

