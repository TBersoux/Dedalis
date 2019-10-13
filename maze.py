import settings
import box
import random

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




    """functions for case...switch statement
    They chose the wall to destroy, following two rules :
    -A wall on the edge of a maze cannot be destroyed
    -A wall separating two boxes with the same group number cannot be destroyed
    """

    def north(self,x,y) :
        if (x!=0) : #first rule
            adjacentBoxGN = self.core[x-1][y].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber:
                self.core[x][y].removeWallNorth()
                self.core[x-1][y].removeWallSouth()

                #let's update the groupNumbers
                if adjacentBoxGN < self.core[x][y].groupNumber:
                    self.core[x][y].groupNumber = adjacentBoxGN
                else:
                    updatedGN = self.core[x][y].groupNumber
                    for coordX in range(settings.COLUMNS) :
                        for coordY in range(settings.ROWS) :
                            if self.core[coordX][coordY].groupNumber == adjacentBoxGN :
                                self.core[coordX][coordY].groupNumber = updatedGN
                
                if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
                    self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !

    def east(self,x,y) :
        if (y!=settings.COLUMNS-1) : #first rule
            adjacentBoxGN = self.core[x][y+1].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber:
                self.core[x][y].removeWallEast()
                self.core[x][y+1].removeWallWest()

                #let's update the groupNumbers
                if adjacentBoxGN < self.core[x][y].groupNumber:
                    self.core[x][y].groupNumber = adjacentBoxGN
                else:
                    updatedGN = self.core[x][y].groupNumber
                    for coordX in range(settings.COLUMNS) :
                        for coordY in range(settings.ROWS) :
                            if self.core[coordX][coordY].groupNumber == adjacentBoxGN :
                                self.core[coordX][coordY].groupNumber = updatedGN
                
                if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
                    self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !

    def south(self,x,y) :
        if (x!=settings.ROWS-1) : #first rule
            adjacentBoxGN = self.core[x+1][y].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber:
                self.core[x][y].removeWallSouth()
                self.core[x+1][y].removeWallNorth()

                #let's update the groupNumbers
                if adjacentBoxGN < self.core[x][y].groupNumber:
                    self.core[x][y].groupNumber = adjacentBoxGN
                else:
                    updatedGN = self.core[x][y].groupNumber
                    for coordX in range(settings.COLUMNS) :
                        for coordY in range(settings.ROWS) :
                            if self.core[coordX][coordY].groupNumber == adjacentBoxGN :
                                self.core[coordX][coordY].groupNumber = updatedGN
                
                if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
                    self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !

    def west(self,x,y) :
        if (y!=0) : #first rule
            adjacentBoxGN = self.core[x][y-1].groupNumber
            if adjacentBoxGN != self.core[x][y].groupNumber:
                self.core[x][y].removeWallWest()
                self.core[x][y-1].removeWallEast()

                #let's update the groupNumbers
                if adjacentBoxGN < self.core[x][y].groupNumber:
                    self.core[x][y].groupNumber = adjacentBoxGN
                else:
                    updatedGN = self.core[x][y].groupNumber
                    for coordX in range(settings.COLUMNS) :
                        for coordY in range(settings.ROWS) :
                            if self.core[coordX][coordY].groupNumber == adjacentBoxGN :
                                self.core[coordX][coordY].groupNumber = updatedGN
                
                if self.core[x][y].groupNumber == 0 : #if our box is in the same group as the enter
                    self.boxesToChange.remove((x,y)) # we remove it from the boxesToChange list, this box is done !
    
    

    #builds the maze, using the 4 earlier functions in a case...switch like statement
    def build(self) :
        while (len(self.boxesToChange) != 0):
            for column in self.core :
                for line in column :
                    print (str(line.groupNumber), end= '')
                print()
            input("Continue ?")
            x,y = random.choice(self.boxesToChange)
            randomWall = random.randint(1,4)
            if randomWall == 1:
                self.north(x,y)
            elif randomWall == 2:
                self.east(x,y)
            elif randomWall == 3:
                self.south(x,y)
            elif randomWall == 4:
                self.west(x,y)

    def drawMap(self):

        column = 0
        row = 0
        for _cpt in range(settings.ROWS*settings.COLUMNS) :
            
            self.map[row][column] = self.core[row][column].walls
            column += 1

            if (column)==settings.COLUMNS : #when we are at the end of the line
                column=0
                row += 1




        









