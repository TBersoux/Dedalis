import settings
import box
import random



#==============Functions==============#

#Create a new Maze and return its map.
def newMaze() :
    createdMaze = Maze()
    createdMaze.build()
    createdMaze.Map()
    return createdMaze.map

#==============Class==============#

#a maze is made of boxes. Two of them are special : an exit, and an enter.


class Maze:
    def __init__(self):
        self.core = [] #the core of the maze contains al the boxes at their right location
        self.map = [] #map of the maze (boxes stored as bytes, see box.py for details)
        self.boxesToChange = [] #list of boxes that are not yet finished, using their coords
        

        #initialization of 2D lists with empty boxes
        for row in range(settings.ROWS) :
            self.core.append([])
            self.map.append([])
            for _column in range(settings.COLUMNS) :
                self.core[row].append(box.Box())
                self.map[row].append([])

        #initialization of their values
        column = 0
        row = 0
        for cpt in range(settings.ROWS*settings.COLUMNS) :
            self.core[row][column].groupNumber = cpt
            self.core[row][column].coordX = row
            self.core[row][column].coordY = column

            self.boxesToChange.append(((row,column))) #Will be useful for building the maze
            column += 1

            if (column)==settings.COLUMNS : #when we are at the end of the line
                column=0
                row += 1
        
        self.core[0][0].makeEnter()
        self.core[settings.ROWS-1][settings.COLUMNS-1].makeExit()
        self.boxesToChange.remove((0,0))


    #This function is used next. 
    #It updates all the boxes groupnumber depending on the groupnumber of the chosen box, and its adjacent box.
    #See Maze.Build() for the choice of the box and its adjacent box. .

    def updateGN(self,adjacentGN,currentGN) :
        if adjacentGN < currentGN:
                    for coordX in range(settings.ROWS) :
                        for coordY in range(settings.COLUMNS) :
                            if self.core[coordX][coordY].groupNumber == currentGN :
                                self.core[coordX][coordY].groupNumber = adjacentGN
        else:
            for coordX in range(settings.ROWS) :
                for coordY in range(settings.COLUMNS) :
                    if self.core[coordX][coordY].groupNumber == adjacentGN :
                        self.core[coordX][coordY].groupNumber = currentGN
        

    """functions for case...switch like statement used in Maze.build()
    They chose the wall to destroy, following two rules :
    -A wall on the edge of a maze cannot be destroyed
    -A wall separating two boxes with the same group number cannot be destroyed
    The three functions are very similar
    """

    def north(self,x,y) :
        if (x!=0) : #first rule
            adjacentBoxGN = self.core[x-1][y].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber: #second rule
                self.core[x][y].removeWallNorth()
                self.core[x-1][y].removeWallSouth()
                self.updateGN(adjacentBoxGN,self.core[x][y].groupNumber)
                
                
        if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
            self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !

    def east(self,x,y) :
        if (y!=settings.COLUMNS-1) : #first rule
            adjacentBoxGN = self.core[x][y+1].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber: #second rule
                self.core[x][y].removeWallEast()
                self.core[x][y+1].removeWallWest()
                self.updateGN(adjacentBoxGN,self.core[x][y].groupNumber)
                
        if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
            self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !

    def south(self,x,y) :
        if (x!=settings.ROWS-1) : #first rule
            adjacentBoxGN = self.core[x+1][y].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber: #second rule
                self.core[x][y].removeWallSouth()
                self.core[x+1][y].removeWallNorth()
                self.updateGN(adjacentBoxGN,self.core[x][y].groupNumber)
                
        if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
            self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !

    def west(self,x,y) :
        if (y!=0) : #first rule
            adjacentBoxGN = self.core[x][y-1].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber: #second rule
                self.core[x][y].removeWallWest()
                self.core[x][y-1].removeWallEast()
                self.updateGN(adjacentBoxGN,self.core[x][y].groupNumber)
                
        if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
            self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !
    
    

    #builds the maze, using the 4 previous functions
    def build(self) :
        while (len(self.boxesToChange) != 0):
            x,y = random.choice(self.boxesToChange)
            randomWall = random.randint(1,4)
            _directions = {1:self.north , 2:self.east , 3:self.south , 4:self.west ,}[randomWall](x,y)


    def Map(self):
        column = 0
        row = 0
        for _cpt in range(settings.ROWS*settings.COLUMNS) :
            self.map[row][column] = self.core[row][column].walls
            column += 1
            if (column)==settings.COLUMNS : #when we are at the end of the line
                column=0
                row += 1




        









