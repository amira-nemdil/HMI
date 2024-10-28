import sys 
from PySide6.QtWidgets import QApplication,QMainWindow,QSpinBox, QWidget,QSlider
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Correctly initialize the base class
        self.setWindowTitle("My App")  # Set the window title
        self.mytext = ''


        widget = QSlider()
        #widget.setMinimum(-10)
        #widget.setMaximum(3)
        widget.setRange(-10,3)
        
        widget.setSingleStep(1) 
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("pressed!")

    def slider_released(self):
        print("Released")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()