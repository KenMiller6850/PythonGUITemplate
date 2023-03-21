# Purpose: Example program written to learn Python.
# Description: Call stored proc from PyQt6 GUI app
# Author: K. Miller
# Date: 2022-06-26


import sys

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QHeaderView,QStatusBar)
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
import pandas as pd
import pyodbc
#from ReadConfig2 import getSQLCONFIG
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table, select,text, inspect
#import interface_icons
from GUITemplate import Ui_MainWindow
import qdarktheme









class Window(QMainWindow, Ui_MainWindow):



    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
             

        self.action_Exit.triggered.connect(self.close)
        
        #self.labelName.setText('')
        #self.labelTitle.setText('')
        #self.labelManager.setText('')
       

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # signal for the pushbutton click
        #self.pushButton.clicked.connect(self.clicked_btn)
        #self.comboServers.currentTextChanged.connect(self.server_changed)
        #self.tabWidget.currentChanged.connect(self.onChange) #changed!
        #self.tablePermissions.clicked.connect(self.on_Click) 
        

       

    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Apply dark theme to Qt application
    app.setStyleSheet(qdarktheme.load_stylesheet())
    
    win = Window()
    win.show()
    
    sys.exit(app.exec())        