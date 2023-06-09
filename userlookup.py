# Form implementation generated from reading ui file 'ui/userlookup.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 661)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tablePermissions = QtWidgets.QTableView(self.centralwidget)
        self.tablePermissions.setGeometry(QtCore.QRect(10, 240, 781, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        self.tablePermissions.setPalette(palette)
        self.tablePermissions.setAlternatingRowColors(True)
        self.tablePermissions.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablePermissions.setSortingEnabled(True)
        self.tablePermissions.setObjectName("tablePermissions")
        self.comboServers = QtWidgets.QComboBox(self.centralwidget)
        self.comboServers.setGeometry(QtCore.QRect(10, 200, 371, 25))
        self.comboServers.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboServers.setStyleSheet("comboServers.setStyleSheet(\"combobox-popup: 0;\");\n"
"selection-color: rgb(222, 234, 255);")
        self.comboServers.setMaxVisibleItems(10)
        self.comboServers.setMinimumContentsLength(25)
        self.comboServers.setObjectName("comboServers")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 611, 151))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tabUserSearch = QtWidgets.QWidget()
        self.tabUserSearch.setObjectName("tabUserSearch")
        self.lineEdit = QtWidgets.QLineEdit(self.tabUserSearch)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tabUserSearch)
        self.label.setGeometry(QtCore.QRect(10, 30, 49, 22))
        self.label.setObjectName("label")
        self.labelName = QtWidgets.QLabel(self.tabUserSearch)
        self.labelName.setGeometry(QtCore.QRect(190, 30, 401, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("")
        self.labelName.setObjectName("labelName")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tabUserSearch)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 90, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tabUserSearch)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 49, 22))
        self.label_3.setObjectName("label_3")
        self.labelName_2 = QtWidgets.QLabel(self.tabUserSearch)
        self.labelName_2.setGeometry(QtCore.QRect(190, 90, 401, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.labelName_2.setFont(font)
        self.labelName_2.setStyleSheet("")
        self.labelName_2.setObjectName("labelName_2")
        self.tabWidget.addTab(self.tabUserSearch, "")
        self.tabGroupSearch = QtWidgets.QWidget()
        self.tabGroupSearch.setObjectName("tabGroupSearch")
        self.edtWindowsGroup = QtWidgets.QLineEdit(self.tabGroupSearch)
        self.edtWindowsGroup.setGeometry(QtCore.QRect(110, 10, 211, 22))
        self.edtWindowsGroup.setObjectName("edtWindowsGroup")
        self.label_2 = QtWidgets.QLabel(self.tabGroupSearch)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 22))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tabGroupSearch, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 30, 111, 31))
        self.pushButton.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/magnifying-glass (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.actionE_xit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Permissions Lookup"))
        self.label.setText(_translate("MainWindow", "User ID :"))
        self.labelName.setText(_translate("MainWindow", "name"))
        self.label_3.setText(_translate("MainWindow", "User ID :"))
        self.labelName_2.setText(_translate("MainWindow", "name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUserSearch), _translate("MainWindow", "Search by User Name"))
        self.label_2.setText(_translate("MainWindow", "Windows Group :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGroupSearch), _translate("MainWindow", "Search by Windows Group"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))
