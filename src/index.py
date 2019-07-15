from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui,_ = loadUiType('../mylib.ui')

# starting of main class
class MainApp (QMainWindow, ui):
    def __init__ (self):
        QMainWindow.__init__(self)
        self.setupUi(self)
    
def main ():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    # call the main function
    main ()