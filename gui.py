import tkinter
import settings
import sys
from PySide2 import QtWidgets #pylint: disable=no-name-in-module
from PySide2.QtUiTools import QUiLoader #pylint: disable=no-name-in-module
from PySide2.QtWidgets import QApplication #pylint: disable=no-name-in-module



def mainWindow_setup(win):
    win.setWindowTitle("Dedalis")


loader = QUiLoader()
app = QApplication(sys.argv)

window = loader.load("mainwindow.ui", None)
mainWindow_setup(window)
window.show()
sys.exit(app.exec_())





#Draw a box on a canvas at given coordinates
def drawBox(Canvas,code,x,y) :
    if code == 0:
        pass
    elif code == 1:
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
    elif code == 2:
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 3:
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 4:
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 5:
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 6:
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 7:
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
    elif code == 8:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
    elif code == 9:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
    elif code == 10:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 11:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
    elif code == 12:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 13:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)
    elif code == 14:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
    elif code == 15:
        Canvas.create_line(x,y,x+settings.BOXSIDE,y)
        Canvas.create_line(x+settings.BOXSIDE,y,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x,y+settings.BOXSIDE,x+settings.BOXSIDE,y+settings.BOXSIDE)
        Canvas.create_line(x,y,x,y+settings.BOXSIDE)

        #==============Tkinter==============#

#Draw a maze on a canvas using its map
def drawMaze(Canvas,map):
    coordX = 55
    coordY = 55
    for column in map :
        for code in column :
            drawBox(Canvas,code,coordX,coordY)
            coordX+=settings.BOXSIDE
        coordX= 55
        coordY+=settings.BOXSIDE



