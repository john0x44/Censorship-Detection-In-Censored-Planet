from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

from backendUI import Ui_MainWindow

#import ui 
import databaseUI
import fileInfoUI
import dashboardUI

import sys 
from backend import ConnectUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # view database info ui, use later
        self.DATABASE_UI_WINDOW=QtWidgets.QMainWindow()
        self.DATABASE_UI=databaseUI.DatabaseUI()
        self.DATABASE_UI.setupUi(self.DATABASE_UI_WINDOW)

        # view file info ui, use later
        self.FILEINFO_UI_WINDOW=QtWidgets.QMainWindow() 
        self.FILEINFO_UI=fileInfoUI.FileInfoUI() 
        self.FILEINFO_UI.setupUi(self.FILEINFO_UI_WINDOW)

        # view dashboard ui, use later
        self.DASHBOARD_UI_WINDOW=QtWidgets.QMainWindow()
        self.DASHBOARD_UI=dashboardUI.DashboardUI()
        self.DASHBOARD_UI.setupUi(self.DASHBOARD_UI_WINDOW)

        #pass in the windows 
        ConnectUI(self.ui,self.FILEINFO_UI,self.DASHBOARD_UI,self.DATABASE_UI)
        self.setWindowTitle("Censorship Detection")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())