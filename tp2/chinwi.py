import sys
import os
import vlc
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")

        # Set layout
        layout = QVBoxLayout()

        # Create button
        self.button = QPushButton('Press me if you are not gay')
        self.button.clicked.connect(self.play_video)  

        # Improve button design by loading stylesheet
        self.load_stylesheet()

        # Set the size of the main window
        self.setFixedSize(600, 500)

        # Add button to layout
        layout.addWidget(self.button)

        # Create a central widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # VLC player instance (we'll initialize it later)
        self.instance = None
        self.player = None

    def load_stylesheet(self):
        stylesheet_path = os.path.join(os.path.dirname(__file__), 'styles.qss')
        with open(stylesheet_path, 'r') as file:
            self.setStyleSheet(file.read())

    def play_video(self):
        video_file = r"E:\stickers and memes\femboy.mp4"

        # OpenCV for video display
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            print("Error opening video file")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)

        # VLC for audio playback
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        media = self.instance.media_new(video_file)
        self.player.set_media(media)
        self.player.play()

        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break

            text = "Ya No9ch"
            font = cv2.FONT_HERSHEY_SIMPLEX
            textsize = cv2.getTextSize(text, font, 1, 2)[0]
            textX = int((width - textsize[0]) / 2)
            textY = int(textsize[1] * 2)
            cv2.putText(frame, text, (textX, textY), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow("Video Player", frame)

            if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        self.player.stop()  # Stop VLC player when video finishes

    def closeEvent(self, event):
        if self.player and self.player.is_playing():
            self.player.stop()
        event.accept() 

app = QApplication([])
window = MainWindow()
window.show()
app.exec()