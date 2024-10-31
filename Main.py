from PySide6 import QtWidgets
from User_Interface import UserInterface
import sys

def Main():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()
if __name__ == "__main__":
    Main()

#* command to turn ui files into py files: pyside6-uic input.ui > output.py 
#! remember to change encoding of the  ui-to-py files to utf-8 EVERY SINGLE TIME
#! REMEMBER YOU HAVE TO DELETE THE OLD PY FILE TO MAKE THE NEW ONE


