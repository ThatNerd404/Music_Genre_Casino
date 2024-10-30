import random 
import PySide6 
from PySide6.QtWidgets import QApplication, QWidget
import sys

def Main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()

if __name__ == "__main__":
    Main()