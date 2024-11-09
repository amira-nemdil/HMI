from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout
from layout_colors import color
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)
        
        layout2.addWidget(color("red"))
        layout2.addWidget(color("black"))
        layout2.addWidget(color("yellow"))
        
        layout3.addWidget(color("pink"))
        layout3.addWidget(color("black"))
       
        
        layout1.addLayout(layout2)
        layout1.addWidget(color("black"))
        layout1.addLayout(layout3)
        
        
        
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        
       

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()