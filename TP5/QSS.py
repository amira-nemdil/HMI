import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Todo")
        self.setFixedSize(300, 400)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Todo list widget
        self.todo_list = QListWidget()
        main_layout.addWidget(self.todo_list)

        # Button layout
        button_layout = QHBoxLayout()

        # Delete button
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_task)
        button_layout.addWidget(self.delete_button)

        # Complete button
        self.complete_button = QPushButton("Complete")
        self.complete_button.clicked.connect(self.complete_task)
        button_layout.addWidget(self.complete_button)

        main_layout.addLayout(button_layout)

        # Input field
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Enter a new todo")
        main_layout.addWidget(self.todo_input)

        # Add button
        self.add_button = QPushButton("Add Todo")
        self.add_button.clicked.connect(self.add_task)
        main_layout.addWidget(self.add_button)

        # Set the main layout and central widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def add_task(self):
        task_text = self.todo_input.text().strip()
        if task_text:
            self.todo_list.addItem(task_text)
            self.todo_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty")

    def delete_task(self):
        selected_task = self.todo_list.currentRow()
        if selected_task >= 0:
            self.todo_list.takeItem(selected_task)
        else:
            QMessageBox.warning(self, "Warning", "No task selected")

    def complete_task(self):
        selected_task = self.todo_list.currentItem()
        if selected_task:
            selected_task.setText(f"✔ {selected_task.text()}")
            font = selected_task.font()
            font.setStrikeOut(True)
            selected_task.setFont(font)
        else:
            QMessageBox.warning(self, "Warning", "No task selected")


# Run the application
app = QApplication(sys.argv)
window = TodoApp()
window.show()
app.exec()