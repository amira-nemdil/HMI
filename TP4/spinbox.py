import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow, QSpinBox, QDoubleSpinBox,QSlider
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        
        Widget = QDoubleSpinBox() # accepts only int values
        
        # Or: widget = QDoubleSpinBox() acceptsf loat values
        widget = QSlider
        Widget.setMinimum(-10)
        Widget.setMaximum(5)
        Widget.setRange (-10, 5)
        
        Widget.setPrefix("$")
        Widget.setSuffix("cent")
        Widget.setSingleStep(1.5) # or 0.5 when we une doublespinbox
        Widget.valueChanged.connect(self.value_changed)
        Widget.textChanged.connect(self.value_changed_str)
        self.setCentralWidget(Widget)
        
        
    def value_changed(self, i):
        print(f'This is the value: {i}')
        
    def value_changed_str(self, s):
        print(f'This is the text: {s}')
        
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()