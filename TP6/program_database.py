import sys 
import sqlite3
import random
from PySide6.QtWidgets import (
    QApplication,QMainWindow,QVBoxLayout,QLineEdit,
    QTableWidget,QTableWidgetItem,QWidget,QLabel,QPushButton
)
from PySide6.QtCore import Qt

#sample product names and prices for generating random data
PRODUCTS=[
    ("Apple",1.20),("Banana",0.80),("Cherry",2.50),
    ("Dates",3.00),("Eggplant",1.75),("Fig",2.25),
    ("Grapes",2.00),("Honeydew",3.50),("Iceberg Lettuce",1.10),
    ("Jalapeno",1.30)
]

#Name of the database file
DATABASE_FILE="products.db"

class ProductAppp(QMainWindow):
    def _init_(self):
        super().init()
        self.setWindowTitle("Product Database")
        self.setGeometry(100 ,100 ,600 , 400)

        #Initialize the SQLite database (file-based) and fill it with data if empty
        self.conn=sqlite3.connect(DATABASE_FILE)
        self.create_table()
        if self.is_table_empty():
            self.insert_random_data(50) # Insert 50 random rows if the table is empty

        #set up the UI
        self.layout=QVBoxLayout()
        self.search_bar=QLineEdit()
        self.search_bar.setPlaceholderText("Search product...")
        
    
        self.table=QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID","Product","Price"])

        self.layout.addWidget(QLabel("Product Database with Search"))
        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.table)

        #Container widget
        container=QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Load initial data
        self.update_table()

    def create_table(self):
        """Creates the products table if it dosen't exist."""
        cursor=self.conn.cursor()
        cursor.execute("""
             CREATE TABLE IF NOT EXISTS products(
             if INTEGER PRIMARY KEY,
             name TEXT,
             price REAL
             )
        """)
        self.conn.commit()