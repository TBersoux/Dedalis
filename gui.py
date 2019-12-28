import settings
import maze

from PySide2 import QtUiTools #pylint: disable=no-name-in-module
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene,QGraphicsView #pylint: disable=no-name-in-module
from PySide2.QtCore import QFile, Qt, QRect #pylint: disable=no-name-in-module
from PySide2.QtGui import QPainter, QBrush, QPen, QScreen #pylint: disable=no-name-in-module
from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self,scene):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = sceneMaze()
        self.ui.editH.setText(str(settings.ROWS))
        self.ui.editW.setText(str(settings.COLUMNS))

    def drawMaze(self):
        drawNewMaze(self.scene,maze.newMaze())
    def clear(self,scene):
        self.scene.clear()
        self.scene.update()

    def setHeight(self):
        settings.ROWS = int(self.ui.editH.text())
    def setWidth(self):
        settings.COLUMNS = int(self.ui.editW.text())

class sceneMaze(QGraphicsScene):
    def __init__(self):
        super(sceneMaze, self).__init__()
        self.penMaze = QPen(Qt.black,3)
        self.penPlayer1 = QPen(Qt.red,1)
        










#Draw a box on a scene at given coordinates
def drawBox(scene,pen,code,x,y) :

#==========Just making sure the boxes are not too close from the side
    scene.addRect(0,0,10,10,QPen(Qt.white,1),QBrush(Qt.white))
    x+=11
    y+=11
#===========================
    if code == 0:
        pass
    elif code == 1:
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)
    elif code == 2:
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 3:
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 4:
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 5:
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 6:
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 7:
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)
    elif code == 8:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
    elif code == 9:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)
    elif code == 10:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 11:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x,y,x,y+settings.BOXSIDE)
    elif code == 12:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 13:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)
    elif code == 14:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
    elif code == 15:
        scene.addLine(x,y,x+settings.BOXSIDE,y,pen)
        scene.addLine(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE,pen)
        scene.addLine(x,y,x,y+settings.BOXSIDE,pen)

        #==============Tkinter==============#

#Draw a maze on a scene using its map
def drawNewMaze(scene,map):
    coordX = 55
    coordY = 55
    for column in map :
        for code in column :
            drawBox(scene,scene.penMaze,code,coordX,coordY)
            coordX+=settings.BOXSIDE
        coordX= 55
        coordY+=settings.BOXSIDE



