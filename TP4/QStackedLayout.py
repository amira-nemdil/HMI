from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QDial,
    QSlider,
    QGridLayout,
    QStackedLayout
    )

import sys
from PySide6.QtWidgets import QWidget
from layout_colors import color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.layout5 = QStackedLayout()
        self.layout5.addWidget(color("pink"))
        self.layout5.addWidget(color("green"))
        self.layout5.addWidget(color("blue"))
        self.layout5.addWidget(color("yellow"))

        self.layout5.setCurrentIndex(1)
        

        btn1 = QPushButton("souwa lahlouwa")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")

        layout2 = QHBoxLayout()
        layout2.addWidget(btn1)
        layout2.addWidget(btn2)
        layout2.addWidget(btn3)
        layout2.addWidget(btn4)

        layout3 = QVBoxLayout()
        layout3.addLayout(self.layout5)
        layout3.addLayout(layout2)

        btn1.clicked.connect(self.changeIndex)
        btn2.clicked.connect(self.changeIndex2)
        btn3.clicked.connect(self.changeIndex3)
        btn4.clicked.connect(self.changeIndex4)






        widget = QWidget()
        widget.setLayout(layout3)
        self.setCentralWidget(widget)


    def changeIndex(self):
        self.layout5.setCurrentIndex(0)

    def changeIndex2(self):
        self.layout5.setCurrentIndex(1)
    
    def changeIndex3(self):
        self.layout5.setCurrentIndex(2)
    
    def changeIndex4(self):
        self.layout5.setCurrentIndex(3)





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()