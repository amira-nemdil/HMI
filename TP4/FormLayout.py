from PySide6.QtGui import QColor,QPalette
from PySide6.QtWidgets import QApplication , QWidget,QFormLayout, QMainWindow,QVBoxLayout,QSpinBox,QComboBox,QHBoxLayout,QLabel,QDial,QLineEdit,QStackedLayout
import sys

class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette=self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form layout example")


        layout= QFormLayout()


        #crate some widgets to add to the form layout
        name_input=QLineEdit()
        age_input= QSpinBox()
        age_input.setRange(0,120)
        gender_input = QComboBox()
        gender_input.addItems(["male","female","no9ch","Blidi","9bayli"])
        address_input=QLineEdit()

        #add widgets to the form layout withb labels 
        layout.addRow("name:", name_input)
        layout.addRow("age:", age_input)
        layout.addRow("gender:", gender_input)
        layout.addRow("address:", address_input)

        #create a xidget to use the layout
        widget= QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        


        

    



#create qapplication and mainwindow instances and start the app
app = QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()