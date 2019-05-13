# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.speedTitle = QtWidgets.QLabel(self.centralwidget)
        self.speedTitle.setObjectName("speedTitle")
        self.gridLayout.addWidget(self.speedTitle, 0, 0, 1, 1)
        self.speed = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy)
        self.speed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed.setDigitCount(5)
        self.speed.setProperty("value", 0.0)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 0, 1, 1, 1)
        self.cadenceTitle = QtWidgets.QLabel(self.centralwidget)
        self.cadenceTitle.setObjectName("cadenceTitle")
        self.gridLayout.addWidget(self.cadenceTitle, 1, 0, 1, 1)
        self.cadence = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cadence.sizePolicy().hasHeightForWidth())
        self.cadence.setSizePolicy(sizePolicy)
        self.cadence.setObjectName("cadence")
        self.gridLayout.addWidget(self.cadence, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bike Sensors"))
        self.speedTitle.setText(_translate("MainWindow", "<h1>Speed (km/h)</h1>"))
        self.cadenceTitle.setText(_translate("MainWindow", "<h1>Cadence (rpm)</h1>"))

