from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resource App")

        # Get base directory
        basedir = os.path.dirname(__file__)

        # Set window icon
        self.setWindowIcon(QIcon(os.path.join(basedir, "icons", "computer-cloud.png")))  # PNG or ICO based on your choice

        # Create button with icon
        self.button = QPushButton("Click Me!")
        self.button.setIcon(QIcon(os.path.join(basedir, "icons", "burn.png")))  # PNG or ICO
        self.button.clicked.connect(self.close)

        # Set the button as the central widget
        self.setCentralWidget(self.button)
        self.resize(200, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    # app_with_resources.spec 
block_cipher = None

a = Analysis(
    ['app_with_resources.py'],  # Your Python script
    pathex=[],
    binaries=[],
    datas=[('C:\nitro\HMI\TP7\iconsicons\computer-cloud.png', 'icons'),
           ('C:\nitro\HMI\TP7\icons\burn.png', 'icons')],  # Explicitly reference your PNG files
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE (
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ResourceApp',  # Name of your app
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want the console to show for debugging
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\nitro\HMI\TP7\icons\computer-cloud.png'  # Ensure this matches the format of your icon (PNG or ICO)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ResourceApp'
)
bootloader_ignore_signals=False,
