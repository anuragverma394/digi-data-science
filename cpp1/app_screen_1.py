import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QFont

from PyQt5 import uic

class Myapp (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ui_path = 'cpp1/app_screen_1.ui'
        uic.loadUi(ui_path,self)
        self.setWindowTitle("My First App")

if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex =Myapp()
    ex.show()
    sys.exit(app.exec_())          