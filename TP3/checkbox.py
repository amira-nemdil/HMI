import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow
class Mainwindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("My App")
        #checkbox widget
        Widget = QCheckBox("This is a checkbox")
        Widget.setCheckState(Qt.checked)
        Widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(Widget)
        def show_state(self, s):
         print(s == Qt.checked)
         print(s)