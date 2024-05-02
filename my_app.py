# напиши здесь код основного приложения и первого экрана
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout 
from PyQt5.QtCore import Qt
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter) 
        self.setLayout(self.layout)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    def connects(self):
        self.button.clicked.connect(self.next_click)

app = QApplication([])
myapp = MainWin()
app.exec_()







