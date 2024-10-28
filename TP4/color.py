from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from layout_colors import color
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QHBoxLayout()
        layout.addWidget(color("red"))
        layout.addWidget(color("black"))
        layout.addWidget(color("yellow"))
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
       

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
