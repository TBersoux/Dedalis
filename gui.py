import globals
import maze
import sys
import player
import random
import time

from PySide2 import QtUiTools #pylint: disable=no-name-in-module
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene,QGraphicsView #pylint: disable=no-name-in-module
from PySide2.QtCore import QFile, Qt, QRect, Signal, QRunnable, QThreadPool, QObject, QTimer #pylint: disable=no-name-in-module
from PySide2.QtGui import QPainter, QBrush, QPen, QScreen, QColor  #pylint: disable=no-name-in-module
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




    #========TAB Generation functions===========

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

    #========TAB Singleplayer functions===========
    def initPlayers(self):
        player1 = player.Player(1)
        player2 = player.Player(2)
        player3 = player.Player(3)
        player4 = player.Player(4)
        self.players = [player1,player2,player3,player4]
        self.scene.addLine(4,4,4,4,self.scene.penPlayer1Trace)
        player1Pos = self.scene.addLine(4,4,4,4,self.scene.penPlayer1)

        self.playersDrawings = [player1Pos]
    
    def initPlayer(self):
        self.initPlayers()

    def randomAI(self):
        self.initPlayers()
        randomAi = RandomAi()
        randomAi.signals.output.connect(self.playerHumanMove)
        self.threadpool.start(randomAi)

    #Direction Buttons

    def buttonUpclicked(self):
        self.playerHumanMove(0)
    def buttonRightclicked(self):
        self.playerHumanMove(1)
    def buttonDownclicked(self):
        self.playerHumanMove(2)
    def buttonLeftclicked(self):
        self.playerHumanMove(3)
        

    #Human players movements
    def playerHumanMove(self,direction,playerNum=1):
        hasMoved = False
        if direction == 0: #North
            hasMoved = self.players[playerNum-1].north(self.savedMaze.map)
        elif direction == 1: #East
            hasMoved = self.players[playerNum-1].east(self.savedMaze.map)
        elif direction == 2: #South
            hasMoved = self.players[playerNum-1].south(self.savedMaze.map)
        elif direction == 3: #West
            hasMoved = self.players[playerNum-1].west(self.savedMaze.map)
        if hasMoved :
            self.playerDraw(direction,playerNum)
            if (self.players[playerNum-1].row == globals.ROWS and self.players[playerNum-1].column == globals.COLUMNS):
                globals.fini = True
            
    #Player movements drawings

    def playerDraw(self,direction,playerNum):
        if direction == 0: #North
            self.scene.removeItem(self.playersDrawings[playerNum-1])
            self.scene.addLine(self.players[playerNum-1].column*globals.BOXSIDE+4,(self.players[playerNum-1].row+1)*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1Trace)
            self.playersDrawings[playerNum-1] = self.scene.addLine(self.players[playerNum-1].column*globals.BOXSIDE+4,(self.players[playerNum-1].row+1)*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1)
        elif direction == 1: #East
            self.scene.removeItem(self.playersDrawings[playerNum-1])
            self.scene.addLine((self.players[playerNum-1].column-1)*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1Trace)
            self.playersDrawings[playerNum-1] = self.scene.addLine((self.players[playerNum-1].column-1)*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1)
        elif direction == 2: #South
            self.scene.removeItem(self.playersDrawings[playerNum-1])
            self.scene.addLine(self.players[playerNum-1].column*globals.BOXSIDE+4,(self.players[playerNum-1].row-1)*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1Trace)
            self.playersDrawings[playerNum-1] = self.scene.addLine(self.players[playerNum-1].column*globals.BOXSIDE+4,(self.players[playerNum-1].row-1)*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1)
        elif direction == 3: #West
            self.scene.removeItem(self.playersDrawings[playerNum-1])
            self.scene.addLine((self.players[playerNum-1].column+1)*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1Trace)
            self.playersDrawings[playerNum-1] = self.scene.addLine((self.players[playerNum-1].column+1)*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.players[playerNum-1].column*globals.BOXSIDE+4,self.players[playerNum-1].row*globals.BOXSIDE+4,self.scene.penPlayer1)




        
# Defining useful graphics objects to draw the maze
class sceneMaze(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.penMaze = QPen(Qt.black,3)

        self.penPlayer1 = QPen(QColor(255, 0, 0),3)
        self.penPlayer1Trace = QPen(QColor(255, 155, 155),3)
        self.penPlayer2 = QPen(QColor(0, 255, 0),3)
        self.penPlayer2Trace = QPen(QColor(155, 255, 155),3)
        self.penPlayer3 = QPen(QColor(0, 0, 255),3)
        self.penPlayer3Trace = QPen(QColor(155, 155, 255),3)
        self.penPlayer4 = QPen(QColor(255, 0, 255),3)
        self.penPlayer4Trace = QPen(QColor(255, 155, 255),3)


        self.changed.connect(self.update)


# Defining signals of the thread Builder
class BuilderSignals(QObject):

    started = Signal()
    finished = Signal()
    result = Signal(maze.Maze)

class aiSignals(QObject):
    started = Signal()
    finished = Signal()
    result = Signal()
    output = Signal(int)

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

class RandomAi(QRunnable):
    def __init__(self,parent=None):
        super(RandomAi, self).__init__()
        self.signals = aiSignals()

    def run(self):
        while(globals.fini == False):
            choix = random.choice(range(4))
            self.signals.output.emit(choix)
            time.sleep(0.01)
        self.signals.finished.emit()





#Draw a box on a scene at given coordinates
def drawBox(scene,pen,code,row,column) :

    if code == 0:
        pass
    elif code == 1:
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)
    elif code == 2:
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 3:
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 4:
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 5:
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 6:
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 7:
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)
    elif code == 8:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
    elif code == 9:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)
    elif code == 10:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 11:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row,column,row,column+globals.BOXSIDE)
    elif code == 12:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 13:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)
    elif code == 14:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
    elif code == 15:
        scene.addLine(row,column,row+globals.BOXSIDE,column,pen)
        scene.addLine(row+globals.BOXSIDE,column,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row,column+globals.BOXSIDE,row+globals.BOXSIDE,column+globals.BOXSIDE,pen)
        scene.addLine(row,column,row,column+globals.BOXSIDE,pen)




if __name__ == "__main__":
#==============Initializations==============#
    globals.init()

#==================GUI======================#

    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(QScreen().availableGeometry().size())

    window.ui.graphicsView.setScene(window.scene)
    window.ui.graphicsView.centerOn(10,0)

    window.showMaximized()

    sys.exit(app.exec_())
