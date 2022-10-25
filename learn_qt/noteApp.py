# sort of noteApp
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton

class EditText(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("MyNotes App")
        self.resize(300,270)
        self.textEdit = QTextEdit()
        self.btnPress = QPushButton("Button")
        
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress)
        self.setLayout(layout)

        self.btnPress.clicked.connect(self.print_msg)
    def print_msg(self):
        self.textEdit.setPlainText("Hallo to multiline text\nthe time Im talking\n\
        come stand a lil bit closer")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EditText()
    win.show()
    sys.exit(app.exec())
