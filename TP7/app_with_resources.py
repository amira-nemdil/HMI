from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton 
from PySide6.QtGui import QIcon 
import sys 
import os

class MainWindow (QMainWindow):
 def __init__(self):
     
  super().__init__() 
  self.setWindowTitle("Resource App")
  
  
 basedir = os.path.dirname(__file__)
 
 # Set window icon 
 self.setWindowIcon(QIcon(os.path.join(basedir, "icons", "app.ico")))
 
 # Create button with icon 
 
 self.button = QPushButton("Click Me!") 
 self.button.setIcon(QIcon(os.path.join(basedir, "icons", "button.png"))) 
 self.button.clicked.connect(self.close)
 self.setCentralWidget(self.button) 
 self.resize(200, 100)

 if __name__ == "__main__": 
     app = QApplication(sys.argv) 
     
     
 window = MainWindow() 
 window.show() 
 sys.exit(app.exec())