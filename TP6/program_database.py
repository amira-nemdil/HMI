import sys
import sqlite3
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit,
    QTableWidget, QTableWidgetItem, QWidget, QLabel, QPushButton
)
from PySide6.QtCore import Qt

# Sample product names and prices for generating random data
PRODUCTS = [
    ("Apple", 1.20), ("Banana", 0.80), ("Cherry", 2.50),
    ("Dates", 3.00), ("Eggplant", 1.75), ("Fig", 2.25),
    ("Grapes", 2.00), ("Honeydew", 3.50), ("Iceberg Lettuce", 1.10),
    ("Jalapeno", 1.30)
]

# Name of the database file
DATABASE_FILE = "products.db"


class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Database")
        self.setGeometry(100, 100, 600, 400)

        # Initialize the SQLite database (file-based) and fill it with data if empty
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.create_table()
        if self.is_table_empty():
            self.insert_random_data(50)  # Insert 50 random rows if the table is empty

        # Set up the UI
        self.layout = QVBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search product...")
        self.search_bar.textChanged.connect(self.update_table)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Product", "Price"])

        self.layout.addWidget(QLabel("Product Database with Search"))
        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.table)

        # Container widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Load initial data
        self.update_table()

    def create_table(self):
        """Creates the products table if it doesn't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        """)
        self.conn.commit()

    def is_table_empty(self):
        """Checks if the products table is empty."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM products")
        count = cursor.fetchone()[0]
        return count == 0

    def insert_random_data(self, rows):
        """Inserts random data into the products table."""
        cursor = self.conn.cursor()
        for _ in range(rows):
            name, price = random.choice(PRODUCTS)
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def update_table(self):
        """Updates the table view based on the search query."""
        search_query = self.search_bar.text()
        cursor = self.conn.cursor()

        if search_query:
            cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search_query + '%',))
        else:
            cursor.execute("SELECT * FROM products")

        rows = cursor.fetchall()
        self.table.setRowCount(len(rows))

        for row_idx, (id_, name, price) in enumerate(rows):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(id_)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(name))
            self.table.setItem(row_idx, 2, QTableWidgetItem(f"${price:.2f}"))

    def closeEvent(self, event):
        """Handle the application close event to close the database connection."""
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec())