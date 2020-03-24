//cell.cpp
//Creation : 21/03/20

#include "maze.hpp"
#include "settings.h"
#include <random>


maze::maze(){

    //Core initialization + Initialization of the array of coords of the cells to modify
    mazeCore.resize(MAX_X);
    coord created;
    for (int x = 0; x < MAX_X; x++)
    {
        created.x = x;
        for (int y = 0; y < MAX_Y; y++)
        {
            cell newCell(x+y*MAX_X+1,x,y);
            mazeCore[x].push_back(newCell);
            created.y = y;
            unreachableCoords.push_back(created);
        }
    }

    mazeCore[0][0].makeEnter();
    mazeCore[MAX_X-1][MAX_Y-1].makeExit();
    
}



maze::~maze(){}

std::vector<std::vector<uint8_t>> maze::get_mazeMap(){return mazeMap;}
std::vector<std::vector<cell>> maze::get_mazeCore(){return mazeCore;}



void maze::updateBuilder(int adjacentGN,int currentGN)
{
    if (adjacentGN < currentGN)
    {
        for (int x = 0; x < MAX_X; x++)
        {
            for (int y = 0; y < MAX_Y ; y++)
            {
                if (mazeCore[x][y].get_groupNumber() == currentGN)
                {
                    mazeCore[x][y].set_groupNumber(adjacentGN);
                }
                
            }
            
        }
        
    }
    else
    {
        for (int x = 0; x < MAX_X; x++)
        {
            for (int y = 0; y < MAX_Y ; y++)
            {
                if (mazeCore[x][y].get_groupNumber() == adjacentGN)
                {
                    mazeCore[x][y].set_groupNumber(currentGN);
                }
                
            }
            
        }
    }
    
    
}


/*
-Cells that are accessible from the enter are in the group 1
-We choose a random wall from a cell which isn't in group 1, and destroy a random adjacent wall following building rules
-We update the GroupNumbers using the previous function :
    - The modified cell is the chosen one. The adjacent is the one sharing the destroyed wall with the modified one.
    - If the modified cell has a smaller GN than the adjacent one, modified cell GN is modified
    - Else, the adjacent cell and all cells in its group get the modified cell's group number
-When all cells are in group 1, the build is done, we draw and return the map */
void maze::build()
{
    //Random init
    std::random_device rd;     
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> uni14(1,4);

    int i = 0;
    while (unreachableCoords.size()>0)
    {
        
        //We choose a random cell and a random direction for the wall to destroy
        std::uniform_int_distribution<int> uniCells(0,unreachableCoords.size()-1);
        int randomNumber = uniCells(rng);
        int x = unreachableCoords[randomNumber].x;
        int y = unreachableCoords[randomNumber].y;
        int chosenWall = uni14(rng);

        switch (chosenWall)
        {
        case 1: //North
            if(y!=0) //Rule #1
            {
                if (mazeCore[x][y-1].get_groupNumber() != mazeCore[x][y].get_groupNumber()) //Rule #2
                {
                    mazeCore[x][y].removeWallNorth();
                    mazeCore[x][y-1].removeWallSouth();
                    updateBuilder(mazeCore[x][y-1].get_groupNumber() , mazeCore[x][y].get_groupNumber());
                }
            }
            break;
        case 2: //East
            if(x!=MAX_X-1) //Rule #1
            {
                if (mazeCore[x+1][y].get_groupNumber() != mazeCore[x][y].get_groupNumber()) //Rule #2
                {
                    mazeCore[x][y].removeWallEast();
                    mazeCore[x+1][y].removeWallWest();
                    updateBuilder(mazeCore[x+1][y].get_groupNumber() , mazeCore[x][y].get_groupNumber());
                }
            }
            break;
        case 3: //South
            if(y!=MAX_Y-1) //Rule #1
            {
                if (mazeCore[x][y+1].get_groupNumber() != mazeCore[x][y].get_groupNumber()) //Rule #2
                {
                    mazeCore[x][y].removeWallSouth();
                    mazeCore[x][y+1].removeWallNorth();
                    updateBuilder(mazeCore[x][y+1].get_groupNumber() , mazeCore[x][y].get_groupNumber());
                }
            }
            break;
        case 4: //West
            if(x!=0) //Rule #1
            {
                if (mazeCore[x-1][y].get_groupNumber() != mazeCore[x][y].get_groupNumber()) //Rule #2
                {
                    mazeCore[x][y].removeWallWest();
                    mazeCore[x-1][y].removeWallEast();
                    updateBuilder(mazeCore[x-1][y].get_groupNumber() , mazeCore[x][y].get_groupNumber());
                }
            }
            break;
        }

        //Let's delete from unreachableCoords all coords from cells in group 1, since they are now reachable
        for (int cpt = 0; cpt < unreachableCoords.size(); cpt++)
        {
            if (mazeCore[unreachableCoords[cpt].x][unreachableCoords[cpt].y].get_groupNumber() == 1)
            {
                unreachableCoords.erase(unreachableCoords.begin()+cpt); //remove the cell (randomNumber-th element)
                unreachableCoords.shrink_to_fit();
                int test = unreachableCoords.size();
                std::cout << test << endl;
            }
        }
        i++;
    }
    std::cout << "i=" << i <<endl;
}



