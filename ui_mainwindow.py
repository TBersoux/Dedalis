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
        MainWindow.resize(1068, 587)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(500, 100))
        self.tabGeneration = QWidget()
        self.tabGeneration.setObjectName(u"tabGeneration")
        self.labelW = QLabel(self.tabGeneration)
        self.labelW.setObjectName(u"labelW")
        self.labelW.setGeometry(QRect(10, 10, 142, 17))
        self.editH = QLineEdit(self.tabGeneration)
        self.editH.setObjectName(u"editH")
        self.editH.setGeometry(QRect(158, 33, 142, 25))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editH.sizePolicy().hasHeightForWidth())
        self.editH.setSizePolicy(sizePolicy2)
        self.editH.setAlignment(Qt.AlignCenter)
        self.editW = QLineEdit(self.tabGeneration)
        self.editW.setObjectName(u"editW")
        self.editW.setGeometry(QRect(10, 33, 142, 25))
        sizePolicy2.setHeightForWidth(self.editW.sizePolicy().hasHeightForWidth())
        self.editW.setSizePolicy(sizePolicy2)
        self.editW.setAlignment(Qt.AlignCenter)
        self.labelH = QLabel(self.tabGeneration)
        self.labelH.setObjectName(u"labelH")
        self.labelH.setGeometry(QRect(158, 10, 142, 17))
        self.buttonDrawMaze = QPushButton(self.tabGeneration)
        self.buttonDrawMaze.setObjectName(u"buttonDrawMaze")
        self.buttonDrawMaze.setGeometry(QRect(306, 33, 127, 25))
        sizePolicy2.setHeightForWidth(self.buttonDrawMaze.sizePolicy().hasHeightForWidth())
        self.buttonDrawMaze.setSizePolicy(sizePolicy2)
        self.buttonDrawMaze.setMaximumSize(QSize(127, 16777215))
        self.labelWait = QLabel(self.tabGeneration)
        self.labelWait.setObjectName(u"labelWait")
        self.labelWait.setGeometry(QRect(439, 33, 597, 25))
        self.tabWidget.addTab(self.tabGeneration, str())
        self.tab_Singleplayer = QWidget()
        self.tab_Singleplayer.setObjectName(u"tab_Singleplayer")
        self.buttonInitPlayer = QPushButton(self.tab_Singleplayer)
        self.buttonInitPlayer.setObjectName(u"buttonInitPlayer")
        self.buttonInitPlayer.setGeometry(QRect(950, 0, 89, 61))
        self.buttonUp = QPushButton(self.tab_Singleplayer)
        self.buttonUp.setObjectName(u"buttonUp")
        self.buttonUp.setGeometry(QRect(90, 0, 89, 25))
        self.buttonLeft = QPushButton(self.tab_Singleplayer)
        self.buttonLeft.setObjectName(u"buttonLeft")
        self.buttonLeft.setGeometry(QRect(0, 20, 89, 25))
        self.buttonRight = QPushButton(self.tab_Singleplayer)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setGeometry(QRect(180, 20, 89, 25))
        self.buttonDown = QPushButton(self.tab_Singleplayer)
        self.buttonDown.setObjectName(u"buttonDown")
        self.buttonDown.setGeometry(QRect(90, 40, 89, 25))
        self.label = QLabel(self.tab_Singleplayer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 50, 271, 17))
        self.tabWidget.addTab(self.tab_Singleplayer, str())

        self.verticalLayout.addWidget(self.tabWidget)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.editW.editingFinished.connect(MainWindow.setWidth)
        self.editH.editingFinished.connect(MainWindow.setHeight)
        self.buttonDrawMaze.clicked.connect(MainWindow.buttonDrawClicked)
        self.buttonUp.clicked.connect(MainWindow.playerUp)
        self.buttonDown.clicked.connect(MainWindow.playerDown)
        self.buttonInitPlayer.clicked.connect(MainWindow.initPlayer)
        self.buttonLeft.clicked.connect(MainWindow.playerLeft)
        self.buttonRight.clicked.connect(MainWindow.playerRight)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelW.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.editH.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.editW.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.labelH.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.buttonDrawMaze.setText(QCoreApplication.translate("MainWindow", u"Draw a new maze", None))
        self.labelWait.setText(QCoreApplication.translate("MainWindow", u"Please wait ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneration), QCoreApplication.translate("MainWindow", u"Generation", None))
        self.buttonInitPlayer.setText(QCoreApplication.translate("MainWindow", u"Init player", None))
        self.buttonUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
#if QT_CONFIG(shortcut)
        self.buttonUp.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.buttonLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
#if QT_CONFIG(shortcut)
        self.buttonLeft.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.buttonRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
#if QT_CONFIG(shortcut)
        self.buttonRight.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.buttonDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
#if QT_CONFIG(shortcut)
        self.buttonDown.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"(Tip : Use your keyboard !)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Singleplayer), QCoreApplication.translate("MainWindow", u"Singleplayer", None))
    # retranslateUi

