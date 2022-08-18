# display a simple dialog
import sys
from PySide6.QtWidgets import (QLineEdit, QLabel, QPushButton, QApplication, QVBoxLayout, QDialog)

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        #create widgets
        self.edit = QLineEdit("Write sth here")
        self.label = QLabel("Your message")
        self.button = QPushButton("Show messages")
        #create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        #set dialog layout
        self.setLayout(layout)
        #add button signal
        self.button.clicked.connect(self.mymsg)

    def mymsg(self):
        print(f"Hello {self.edit.text()}")
        self.label.setText(self.edit.text())

if __name__ == "__main__":
    #create the qt app
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    #run
    sys.exit(app.exec())
