import box
import maze
import settings
import tkinter



#==============Initializations==============#

settings.init()
canvasHeight = (settings.COLUMNS+1)*settings.BOXSIDE
canvasWidth = (settings.ROWS+1)*settings.BOXSIDE

#==============Functions==============#

#Create a new Maze and return its map
def newMaze() :
    createdMaze = maze.Maze()
    createdMaze.build()
    createdMaze.Map()
    return createdMaze.map

#Draw a box on a given canvas at given coordinates
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

#Draw all the maze on a given canvas
def drawMaze(Canvas):
    coordX = 55
    coordY = 55
    mazeMap = newMaze()
    for column in mazeMap :
        for code in column :
            drawBox(Canvas,code,coordX,coordY)
            coordX+=settings.BOXSIDE
        coordX= 55
        coordY+=settings.BOXSIDE



#==============Tkinter==============#
root = tkinter.Tk()

#Frame init
window = tkinter.Frame(root,  height = 1000, width = 1000)
window.pack(side = "bottom", fill = "x")

#Buttons init
b_NewMaze = tkinter.Button(root, text = "Draw a new maze", command = lambda : drawMaze(Canvas))
b_NewMaze.pack(side = "top")
b_NewMaze.pack(side = "left")
b_Reset = tkinter.Button(root, text = "Reset", command = lambda : Canvas.delete("all"))
b_Reset.pack(side = "top")
b_Reset.pack(side = "right")

#Canvas init
Canvas = tkinter.Canvas(window , bg = "white", height = 800 , width = 800 , scrollregion = (0,0,canvasHeight+100,canvasWidth+100) , xscrollincrement = settings.BOXSIDE , yscrollincrement = settings.BOXSIDE)
Canvas.pack(side = "bottom" , fill = "both")

#Scroll the canvas using arrows
Canvas.bind("<Left>",  lambda event: Canvas.xview_scroll(-1, "units"))
Canvas.bind("<Right>", lambda event: Canvas.xview_scroll( 1, "units"))
Canvas.bind("<Up>",    lambda event: Canvas.yview_scroll(-1, "units"))
Canvas.bind("<Down>",  lambda event: Canvas.yview_scroll( 1, "units"))

#Set focus on the canvas, a click on the canvas focus it again
Canvas.focus_set()
Canvas.bind("<Button-1>", lambda event: Canvas.focus_set())

root.mainloop()

