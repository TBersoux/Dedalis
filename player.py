# A player walk through the maze. He has a number (1 to 4), a type (Human or AI), a position and a finished status.

class Player:
    def __init__(self,number=1,human=True,row=0,column=0):
        self.number = number
        self.human = True
        self.row = row
        self.column = column
        self.finished = False

    #Move player and return True if the move has been made
    def north(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00001000) != 0b00001000)) :
            self.row -= 1
            return True
        else :
            return False


    def south(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00000010) != 0b00000010)) :
            self.row += 1
            return True
        else :
            return False

    def west(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00000001) != 0b00000001) and self.row+ self.column !=0):
            self.column -= 1
            return True
        else :
            return False

    def east(self,mazeMap):
        if(((mazeMap[self.row][self.column] & 0b00000100) != 0b00000100)) :
            self.column += 1
            return True
        else :
            return False