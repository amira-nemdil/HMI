from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon 
import sys
import os
class MainWindow(QMainWindow):
    
 def __init__(self):
  self.setWindowTitle("Basic App")
  self.button = QPushButton("Click Me!")
  self.button.clicked.connect(self.close) 
  self.setCentralWidget(self.button) 
  self.resize(200, 100)
 
 if __name__ == "__main__": 
   app = QApplication(sys.argv)
 
 window = QMainWindow()

 window.show() 

 sys.exit(app.exec())