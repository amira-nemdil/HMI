import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTableWidget, \
    QTableWidgetItem, QPushButton, QLabel, QComboBox
import sys


class DatabaseApp(QMainWindow):
    def __init__(self, db_path):
        super().__init__()
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SQLite Database Viewer")

        # Main widget and layout
        main_widget = QWidget()
        layout = QVBoxLayout()

        # Table selection dropdown
        self.table_select = QComboBox()
        self.table_select.addItems(self.get_table_names())
        self.table_select.currentTextChanged.connect(self.load_table_data)
        layout.addWidget(QLabel("Select Table:"))
        layout.addWidget(self.table_select)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter search term...")
        layout.addWidget(self.search_bar)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_table)
        layout.addWidget(self.search_button)

        # Table widget to display data
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Load initial table data
        self.load_table_data()

    def get_table_names(self):
        # Fetch table names from the database
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

    def load_table_data(self):
        # Load data from the selected table
        table_name = self.table_select.currentText()
        self.cursor.execute(f"SELECT * FROM {table_name}")
        data = self.cursor.fetchall()
        headers = [description[0] for description in self.cursor.description]

        # Populate table widget
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                self.table_widget.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))

    def search_table(self):
        # Perform search within the selected table
        search_term = self.search_bar.text()
        table_name = self.table_select.currentText()

        # Example of a simple search by applying search_term to all columns (modify as needed)
        query = f"SELECT * FROM {table_name} WHERE "
        query += " OR ".join([f"{col} LIKE ?" for col in [desc[0] for desc in self.cursor.description]])
        search_query = [f"%{search_term}%"] * len(self.cursor.description)

        self.cursor.execute(query, search_query)
        data = self.cursor.fetchall()

        # Display search results
        self.table_widget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                self.table_widget.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))


def main():
    app = QApplication(sys.argv)
    db_path = "C:\Softwares\DB Browser for SQLite\Chinook_Sqlite.sqlite"
    window = DatabaseApp(db_path)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()