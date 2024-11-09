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
    QGridLayout
    )

import sys
from PySide6.QtWidgets import QWidget
from layout_colors import color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(color("red"), 0,0)
        layout.addWidget(color("cyan"), 1,0)
        layout.addWidget(color("teal"), 1,1)
        layout.addWidget(color("grey"), 2,1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)






app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()