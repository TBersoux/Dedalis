# A player walk through the maze. He has a number (1 to 4), a type (Human or AI), a position and settings.

class Player:
    def __init__(self,number=1,human=True,row=0,column=0):
        self.number = number
        self.human = True
        self.row = row
        self.column = column

    #Move player and return True if the move has been made
    def up(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00001000) != 0b00001000)) :
            self.row -= 1
            return True
        else :
            return False


    def down(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00000010) != 0b00000010)) :
            self.row += 1
            return True
        else :
            return False

    def left(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00000001) != 0b00000001) and self.row+ self.column !=0):
            self.column -= 1
            return True
        else :
            return False

    def right(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00000100) != 0b00000100)) :
            self.column += 1
            return True
        else :
            return False