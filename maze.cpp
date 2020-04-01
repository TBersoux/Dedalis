//cell.cpp
//Creation : 21/03/20

#include "maze.hpp"
#include "settings.h"
#include <random>


maze::maze(int x,int y)
{
    MAX_X = x;
    MAX_Y = y;
    //Core and map initialization + Initialization of the array of coords of the cells to modify
    mazeCore.resize(MAX_X);
    mazeMap.resize(MAX_X);
    for (int x = 0; x < MAX_X; x++)
    {
        mazeMap[x].resize(MAX_Y);
        for (int y = 0; y < MAX_Y; y++)
        {
            mazeCore[x].emplace_back(x+y*MAX_X+1,x,y);
            unreachableCoords.emplace(x,y);
        }
    }

    mazeCore[0][0].makeEnter();
    unreachableCoords.erase({0,0});
    mazeCore[MAX_X-1][MAX_Y-1].makeExit();
    
}



maze::~maze(){}

std::vector<std::vector<uint8_t>> maze::get_mazeMap(){return mazeMap;}
std::vector<std::vector<cell>> maze::get_mazeCore(){return mazeCore;}
int maze::get_MAX_X(){return MAX_X;}
int maze::get_MAX_Y(){return MAX_Y;}
void maze::set_MAX_X(int x){MAX_X = x;}
void maze::set_MAX_Y(int y){MAX_Y = y;}


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
                    if (adjacentGN == 1) //GN=1 means that the cell is reachable, as it's the GN of the enter
                    {
                        unreachableCoords.erase({x,y});
                    }
                    
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
                    if (currentGN == 1)
                    {
                        unreachableCoords.erase({x,y});
                    }
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

    int cpt = 0;
    while (unreachableCoords.size()>0)
    {
        //We choose a random cell and a random direction for the wall to destroy
        std::uniform_int_distribution<int> uniCells(0,unreachableCoords.size()-1);
        int randomNumber = uniCells(rng);
        auto iter = unreachableCoords.begin();
        advance(iter,randomNumber);
        int x = (*iter).first;
        int y = (*iter).second;
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
        cpt++;
    }

    //Now that the maze is built, we draw the map
    for (unsigned x = 0; x < mazeCore.size(); x++)
    {
        for (unsigned y = 0; y < mazeCore[x].size(); y++)
        {
            mazeMap[x][y] = mazeCore[x][y].get_walls();
        }
            
    }

    std::cout << "Number of modification turns : " << cpt <<endl;


}



