import globals
import maze
import threading

from PySide2 import QtUiTools #pylint: disable=no-name-in-module
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene,QGraphicsView #pylint: disable=no-name-in-module
from PySide2.QtCore import QFile, Qt, QRect, Signal, QRunnable, QThreadPool, QObject #pylint: disable=no-name-in-module
from PySide2.QtGui import QPainter, QBrush, QPen, QScreen  #pylint: disable=no-name-in-module
from ui_mainwindow import Ui_MainWindow




#Base class imported from ui_mainwindow.py, created with qt designer
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = sceneMaze()
        
        self.ui.editH.setText(str(globals.ROWS))
        self.ui.editW.setText(str(globals.COLUMNS))
        self.ui.labelWait.hide()

        self.threadpool = QThreadPool()


    def setHeight(self):
        globals.ROWS = int(self.ui.editH.text())
        
    def setWidth(self):
        globals.COLUMNS = int(self.ui.editW.text())

    # save in mainWindow the maze passed in parameters, then draws it by drawing all its boxes (see under classes)
    def saveAndDrawMaze(self,maze):
        self.savedMaze = maze
        mazeMap = self.savedMaze.map

        coordX = 0
        coordY = 0
        for column in mazeMap :
            for code in column :
                drawBox(self.scene,self.scene.penMaze,code,coordX,coordY)
                coordX+=globals.BOXSIDE
            coordX= 0
            coordY+=globals.BOXSIDE


    #Use a thread (QRunnable from PySide2) as building the maze is a heavy task.
    def buttonDrawClicked(self):
        self.scene.clear()
        self.scene.update()

        builder = Builder()
        builder.signals.started.connect(self.ui.labelWait.show)
        builder.signals.finished.connect(self.ui.labelWait.hide)
        builder.signals.result.connect(self.saveAndDrawMaze)

        self.threadpool.start(builder)



        
# Defining useful graphics objects to draw the maze
class sceneMaze(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.penMaze = QPen(Qt.black,3)
        self.penPlayer1 = QPen(Qt.red,1)


# Defining signals of the thread Builder
class BuilderSignals(QObject):

    started = Signal()
    finished = Signal()
    result = Signal(maze.Maze)

# Defining the thread Builder
class Builder(QRunnable):
    def __init__(self,parent=None):
        super(Builder, self).__init__()
        self.signals = BuilderSignals()

    def run(self):
        self.signals.started.emit()
        createdMaze = maze.Maze()
        createdMaze.build()
        createdMaze.Map()
        self.signals.result.emit(createdMaze)
        self.signals.finished.emit()



#Draw a box on a scene at given coordinates
def drawBox(scene,pen,code,x,y) :

#Just making sure the boxes are not too close from the sides by adding an invisible rectangle
    scene.addRect(0,0,10,10,QPen(Qt.white,1),QBrush(Qt.white))
    x+=11
    y+=11
#===========================
    if code == 0:
        pass
    elif code == 1:
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)
    elif code == 2:
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 3:
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 4:
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 5:
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 6:
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 7:
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)
    elif code == 8:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
    elif code == 9:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)
    elif code == 10:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 11:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x,y,x,y+globals.BOXSIDE)
    elif code == 12:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 13:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)
    elif code == 14:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
    elif code == 15:
        scene.addLine(x,y,x+globals.BOXSIDE,y,pen)
        scene.addLine(x+globals.BOXSIDE,y,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x,y+globals.BOXSIDE,x+globals.BOXSIDE,y+globals.BOXSIDE,pen)
        scene.addLine(x,y,x,y+globals.BOXSIDE,pen)





