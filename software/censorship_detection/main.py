from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

from UI.backendUI import Ui_MainWindow

#import ui

from UI import databaseUI
from UI import fileInfoUI
from UI import dashboardUI
from UI import filterTimeUI
from UI import scoreReportUI 
from UI import domainSearchUI
from UI import countrySearchUI 

import sys 
from backend import ConnectUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Load UI into memory - use them later 
        # domainSearch UI, use later
        self.DOMAINSEARCH_UI_WINDOW = QtWidgets.QMainWindow() 
        self.DOMAINSEARCH_UI = domainSearchUI.DomainSearchUI() 
        self.DOMAINSEARCH_UI.setupUi(self.DOMAINSEARCH_UI_WINDOW)

        # countrySearch UI, use later 

        self.COUNTRYSEARCH_UI_WINDOW = QtWidgets.QMainWindow() 
        self.COUNTRYSEARCH_UI = countrySearchUI.CountrySearchUI() 
        self.COUNTRYSEARCH_UI.setupUi(self.COUNTRYSEARCH_UI_WINDOW)

        # view scoreReport Ui, use later 
        self.SCOREREPORT_UI_WINDOW = QtWidgets.QMainWindow()
        self.SCOREREPORT_UI = scoreReportUI.ScoreReportUI() 
        self.SCOREREPORT_UI.setupUi(self.SCOREREPORT_UI_WINDOW)

        # view filterTime ui, use later 
        self.FILTERTIME_UI_WINDOW = QtWidgets.QMainWindow()
        self.FILTERTIME_UI = filterTimeUI.FilterTimeUI() 
        self.FILTERTIME_UI.setupUi(self.FILTERTIME_UI_WINDOW)

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
        ConnectUI(self.ui,self.FILEINFO_UI,self.DASHBOARD_UI,self.DATABASE_UI,self.FILTERTIME_UI,self.SCOREREPORT_UI,self.DOMAINSEARCH_UI,self.COUNTRYSEARCH_UI)
        self.setWindowTitle("Censorship Detection")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())