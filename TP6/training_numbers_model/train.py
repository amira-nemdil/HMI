import sys
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QWidget, QHBoxLayout, QMessageBox, QTabWidget,
    QProgressBar, QSpinBox, QProgressDialog
)
from PySide6.QtGui import QPixmap, QPainter, QPen, QImage
from PySide6.QtCore import Qt, QPoint, Signal, QThread
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from PIL import Image
import cv2
import joblib
import os


class ModelTrainer(QThread):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        try:
            # Fetch MNIST dataset
            mnist = fetch_openml('mnist_784', version=1)
            X, y = mnist.data / 255.0, mnist.target.astype(int)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Create and train the model
            self.model = MLPClassifier(
                hidden_layer_sizes=(256, 128),
                activation='relu',
                solver='adam',
                batch_size=256,
                learning_rate='adaptive',
                max_iter=50,
                verbose=True,
                random_state=42
            )

            # Train with progress updates
            n_iters = self.model.max_iter
            for i in range(n_iters):
                self.model.partial_fit(X_train, y_train, classes=np.unique(y))
                self.progress.emit(int((i + 1) * 100 / n_iters))

            # Save the model
            if not os.path.exists('models'):
                os.makedirs('models')
            joblib.dump(self.model, 'models/mnist_model.pkl')

            self.finished.emit()
        except Exception as e:
            print(f"Training error: {e}")


class DrawingCanvas(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(80, 80)
        self.setStyleSheet("background-color: black; border: 2px solid #cccccc;")
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.black)
        self.drawing = False
        self.last_point = QPoint()
        self.pen_width = 5

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()
            painter = QPainter(self.image)
            pen = QPen(Qt.white, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawPoint(self.last_point)
            self.update()

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.white, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            current_point = event.position().toPoint()
            painter.drawLine(self.last_point, current_point)
            self.last_point = current_point
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def clear_canvas(self):
        self.image.fill(Qt.black)
        self.update()

    def get_image_data(self):
        # Convert QImage to numpy array
        buffer = self.image.bits().tobytes()
        arr = np.frombuffer(buffer, np.uint8).reshape((self.height(), self.width(), 4))

        # Convert to grayscale
        gray = cv2.cvtColor(arr, cv2.COLOR_RGBA2GRAY)

        # Apply thresholding
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Find the bounding box of the digit
        coords = cv2.findNonZero(binary)
        if coords is None:
            return np.zeros((1, 784))

        x, y, w, h = cv2.boundingRect(coords)

        # Add padding
        size = max(w, h) + 20
        top = max(0, y - (size - h) // 2)
        bottom = min(self.height(), top + size)
        left = max(0, x - (size - w) // 2)
        right = min(self.width(), left + size)

        cropped = binary[top:bottom, left:right]

        # Resize to 28x28
        resized = cv2.resize(cropped, (28, 28), interpolation=cv2.INTER_AREA)

        # Normalize
        normalized = resized.astype('float32') / 255.0
        return normalized.reshape(1, -1)


class IMNISTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enhanced MNIST Recognition")
        self.setGeometry(100, 100, 800, 500)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Model training section
        training_widget = QWidget()
        training_layout = QHBoxLayout(training_widget)

        self.train_button = QPushButton("Train New Model")
        self.train_button.clicked.connect(self.train_model)
        training_layout.addWidget(self.train_button)

        self.load_button = QPushButton("Load Existing Model")
        self.load_button.clicked.connect(self.load_model)
        training_layout.addWidget(self.load_button)

        self.model_status = QLabel("Model Status: Not Loaded")
        training_layout.addWidget(self.model_status)

        main_layout.addWidget(training_widget)

        # Tabs
        self.tabs = QTabWidget()
        self.init_tabs()
        main_layout.addWidget(self.tabs)

        # Initialize model trainer
        self.trainer = None
        self.model = None

        # Try to load existing model
        if os.path.exists('models/mnist_model.pkl'):
            self.load_model()

    def init_tabs(self):
        # Upload tab
        self.upload_tab = QWidget()
        upload_layout = QVBoxLayout()

        self.test_button = QPushButton("Upload Test Image")
        self.test_button.clicked.connect(self.upload_image)
        self.test_button.setEnabled(False)
        upload_layout.addWidget(self.test_button)

        self.image_label = QLabel("No image uploaded.")
        self.image_label.setAlignment(Qt.AlignCenter)
        upload_layout.addWidget(self.image_label)

        self.result_label = QLabel("Predicted Number: ")
        self.result_label.setAlignment(Qt.AlignCenter)
        upload_layout.addWidget(self.result_label)

        self.upload_tab.setLayout(upload_layout)

        # Draw tab
        self.draw_tab = QWidget()
        draw_layout = QVBoxLayout()

        self.canvas = DrawingCanvas()
        draw_layout.addWidget(self.canvas, alignment=Qt.AlignCenter)

        button_layout = QHBoxLayout()

        self.predict_button = QPushButton("Predict Drawing")
        self.predict_button.clicked.connect(self.predict_drawing)
        self.predict_button.setEnabled(False)
        button_layout.addWidget(self.predict_button)

        self.clear_button = QPushButton("Clear Drawing")
        self.clear_button.clicked.connect(self.canvas.clear_canvas)
        button_layout.addWidget(self.clear_button)

        draw_layout.addLayout(button_layout)

        self.draw_result_label = QLabel("Predicted Number: ")
        self.draw_result_label.setAlignment(Qt.AlignCenter)
        draw_layout.addWidget(self.draw_result_label)

        self.draw_tab.setLayout(draw_layout)

        # Add tabs
        self.tabs.addTab(self.upload_tab, "Upload Image")
        self.tabs.addTab(self.draw_tab, "Draw Number")

    def train_model(self):
        # Create progress dialog
        progress = QProgressDialog("Training model...", "Cancel", 0, 100, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.setAutoClose(True)

        # Create and start trainer thread
        self.trainer = ModelTrainer()
        self.trainer.progress.connect(progress.setValue)
        self.trainer.finished.connect(self.training_finished)
        self.trainer.start()

    def training_finished(self):
        self.model = joblib.load('models/mnist_model.pkl')
        self.model_status.setText("Model Status: Trained")
        self.test_button.setEnabled(True)
        self.predict_button.setEnabled(True)
        QMessageBox.information(self, "Success", "Model training completed!")

    def load_model(self):
        try:
            self.model = joblib.load('models/mnist_model.pkl')
            self.model_status.setText("Model Status: Loaded")
            self.test_button.setEnabled(True)
            self.predict_button.setEnabled(True)
            QMessageBox.information(self, "Success", "Model loaded successfully!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load model: {str(e)}")

    def upload_image(self):
        if self.model is None:
            QMessageBox.warning(self, "Error", "Please load or train a model first!")
            return

        file_path, _ = QFileDialog.getOpenFileName(self, "Select an Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            image = Image.open(file_path).convert("L")
            image = image.resize((28, 28))
            image_array = np.array(image).reshape(1, -1) / 255.0

            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))

            prediction = self.model.predict(image_array)[0]
            confidence = np.max(self.model.predict_proba(image_array)) * 100
            self.result_label.setText(f"Predicted Number: {prediction} (Confidence: {confidence:.2f}%)")

    def predict_drawing(self):
        if self.model is None:
            QMessageBox.warning(self, "Error", "Please load or train a model first!")
            return

        image_array = self.canvas.get_image_data()
        prediction = self.model.predict(image_array)[0]
        confidence = np.max(self.model.predict_proba(image_array)) * 100
        self.draw_result_label.setText(f"Predicted Number: {prediction} (Confidence: {confidence:.2f}%)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IMNISTApp()
    window.show()
    sys.exit(app.exec())