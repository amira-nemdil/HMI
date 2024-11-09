import sys 
from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget
)
from layout_colors import color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        tabs = QTabWidget()
        #tab.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        # Add tabs with different colors
        for Color in ["red", "green", "blue","yellow"]:
            tabs.addTab(color(Color), Color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()