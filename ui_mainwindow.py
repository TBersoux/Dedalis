# -*- coding: utf-8 -*-

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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelW = QLabel(self.centralwidget)
        self.labelW.setObjectName(u"labelW")

        self.gridLayout.addWidget(self.labelW, 0, 0, 1, 1)

        self.labelH = QLabel(self.centralwidget)
        self.labelH.setObjectName(u"labelH")

        self.gridLayout.addWidget(self.labelH, 0, 2, 1, 1)

        self.editH = QLineEdit(self.centralwidget)
        self.editH.setObjectName(u"editH")

        self.gridLayout.addWidget(self.editH, 1, 2, 1, 1)

        self.buttonClear = QPushButton(self.centralwidget)
        self.buttonClear.setObjectName(u"buttonClear")

        self.gridLayout.addWidget(self.buttonClear, 2, 2, 1, 1)

        self.buttonDrawMaze = QPushButton(self.centralwidget)
        self.buttonDrawMaze.setObjectName(u"buttonDrawMaze")

        self.gridLayout.addWidget(self.buttonDrawMaze, 2, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 3, 0, 1, 3)

        self.editW = QLineEdit(self.centralwidget)
        self.editW.setObjectName(u"editW")

        self.gridLayout.addWidget(self.editW, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonDrawMaze.clicked.connect(MainWindow.drawMaze)
        self.buttonClear.clicked.connect(MainWindow.clear)
        self.editW.editingFinished.connect(MainWindow.setWidth)
        self.editH.editingFinished.connect(MainWindow.setHeight)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelW.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.labelH.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.editH.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.buttonClear.setText(QCoreApplication.translate("MainWindow", u"Clear drawing", None))
        self.buttonDrawMaze.setText(QCoreApplication.translate("MainWindow", u"Draw a new maze", None))
        self.editW.setText(QCoreApplication.translate("MainWindow", u"40", None))
    # retranslateUi

