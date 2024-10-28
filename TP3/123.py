import sys
from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        # Create QListWidget widget
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
        
        # In QListWidget there are two separate signals for the item and the string
        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)
        
        # Set the widget as the central widget
        self.setCentralWidget(widget)

    # Slot to handle current item change (i is a QListWidgetItem)
    def item_changed(self, current, previous):  
        if current:  # Check if current item is not None
            print(current.text())
        if previous:  # This is optional, you can remove if not needed
            print(f"Previous: {previous.text()}")

    # Slot to handle current text change
    def text_changed(self, s):  # s is a str
        print(s)

# Create the application and window
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec