from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

from backendUI import Ui_MainWindow
import fileInfoUI

import sys 
from backend import ConnectUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.FILEINFO_UI_WINDOW=QtWidgets.QMainWindow() 
        self.FILEINFO_UI=fileInfoUI.FileInfoUI() 
        self.FILEINFO_UI.setupUi(self.FILEINFO_UI_WINDOW)
        #pass in the windows 
        ConnectUI(self.ui,self.FILEINFO_UI)
        self.setWindowTitle("Censorship Detection")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())