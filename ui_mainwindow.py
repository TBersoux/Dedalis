# -*- coding: utf-8 -*-

#pylint: disable-all
################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.buttonReset = QPushButton(self.centralwidget)
        self.buttonReset.setObjectName(u"buttonReset")

        self.gridLayout.addWidget(self.buttonReset, 3, 2, 1, 1)

        self.buttonDraw = QPushButton(self.centralwidget)
        self.buttonDraw.setObjectName(u"buttonDraw")

        self.gridLayout.addWidget(self.buttonDraw, 3, 1, 1, 1)

        self.editH = QLineEdit(self.centralwidget)
        self.editH.setObjectName(u"editH")

        self.gridLayout.addWidget(self.editH, 1, 2, 1, 1)

        self.labelW = QLabel(self.centralwidget)
        self.labelW.setObjectName(u"labelW")

        self.gridLayout.addWidget(self.labelW, 0, 1, 1, 1)

        self.labelH = QLabel(self.centralwidget)
        self.labelH.setObjectName(u"labelH")

        self.gridLayout.addWidget(self.labelH, 0, 2, 1, 1)

        self.editW = QLineEdit(self.centralwidget)
        self.editW.setObjectName(u"editW")

        self.gridLayout.addWidget(self.editW, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 4, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1052, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonDraw.clicked.connect(MainWindow.drawMaze)
        self.buttonReset.clicked.connect(MainWindow.reset)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dedalis", None))
        self.buttonReset.setText(QCoreApplication.translate("MainWindow", u"Erase drawing", None))
        self.buttonDraw.setText(QCoreApplication.translate("MainWindow", u"Draw a new maze", None))
        self.editH.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.labelW.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.labelH.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.editW.setText(QCoreApplication.translate("MainWindow", u"25", None))
    # retranslateUi

