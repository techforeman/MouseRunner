# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mouserunner_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 131)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(324, 105))
        MainWindow.setMaximumSize(QtCore.QSize(324, 105))
        MainWindow.setWindowOpacity(4.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 301, 91))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 261, 21))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.minimizeToTrayEnabled = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.minimizeToTrayEnabled.setObjectName("minimizeToTrayEnabled")
        self.verticalLayout.addWidget(self.minimizeToTrayEnabled)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.currentTimerValue = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.currentTimerValue.setObjectName("currentTimerValue")
        self.gridLayout.addWidget(self.currentTimerValue, 0, 1, 1, 1)
        self.currentTimerLabel = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.currentTimerLabel.setObjectName("currentTimerLabel")
        self.gridLayout.addWidget(self.currentTimerLabel, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(140, 50, 161, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mouse Runner"))
        self.groupBox.setTitle(_translate("MainWindow", "Menu"))
        self.minimizeToTrayEnabled.setText(_translate("MainWindow", "Minimize to Tray on close window"))
        self.currentTimerValue.setText(_translate("MainWindow", "00:00:00"))
        self.currentTimerLabel.setText(_translate("MainWindow", "Timer: "))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
