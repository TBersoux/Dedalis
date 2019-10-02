#box.py



class Box: #a box is a simple 2D object with 4 walls. It can also be an enter or an exit.

   


    def __init__(self):

        self.groupNumber = 0
        self.isEnter = False
        self.isExit = False
        self.coordX = 0
        self.coordY = 0

        #State of the walls are stocked as a 8it byte : Each bit from the 4 lasts refer to a wall, in this order : North,East,South,West
        #A wall at "1" is up
        self.walls= 0b00001111

    #wall removers
    def removeWallNorth(self):
        self.walls = self.walls & 0b00000111

    def removeWallEast(self):
        self.walls = self.walls & 0b00001011

    def removeWallSouth(self):
        self.walls = self.walls & 0b00001101

    def removeWallWest(self):
        self.walls = self.walls & 0b00001110


    #make that box the enter
    def makeEnter(self):
        self.isEnter=True
        self.removeWallWest()

    #make that box the exit
    def makeExit(self):
        self.isExit = True
        self.removeWallEast()


    
