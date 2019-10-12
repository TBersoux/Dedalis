import settings
import box

#a maze is made of boxes. Two of them are special : an exit, and an enter.


class Maze:
    def __init__(self):
        self.core = [] #the core of the maze contains al the boxes at their right location
        self.map = [] #map of the maze (boxes stored as bytes, see box.py for details)
        self.boxesToChange = [] #list of boxes that are not yet finished, using their coords
        

        #initialization of 2D lists with empty boxes
        for row in range(settings.ROWS) :
            self.core.append([])
            for _column in range(settings.COLUMNS) :
                self.core[row].append(box.Box())

        #initialization of their values
        column = 0
        row = 0
        for cpt in range(settings.ROWS*settings.COLUMNS) :
            self.core[row][column].groupNumber = cpt
            print(str(self.core[row][column].groupNumber))
            self.core[row][column].coordX = row
            self.core[row][column].coordY = column
            self.boxesToChange.append(((row,column)))
            column += 1

            if (column)==settings.COLUMNS : #when we are at the end of the line
                column=0
                row += 1



        for row in self.core :
            for column in row :
                print(str(column.groupNumber), end= '')
            print(end='\n')
        print(str( self.core[1][1].groupNumber))
