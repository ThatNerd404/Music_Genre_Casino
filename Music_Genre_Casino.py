import random 
import PySide6 
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
import sys

def Main():
    loader = QUiLoader()
    app = QApplication(sys.argv)
    window = loader.load("MainWindow.ui", None)
    window.show()
    window.setWindowTitle("Music Genre Casino")
    app.exec()

if __name__ == "__main__":
    Main()