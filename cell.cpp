//cell.cpp
//Creation : 09/03/20

#include "cell.hpp"

cell::cell(int groupN, int X,int Y) //No check on inputs, as the user shouldn't build a cell itself.
{
    groupNumber = groupN;
    coords = std::make_pair(X,Y);
    isEntrance = false;
    isExit = false;

}
cell::~cell(){}

int cell::get_groupNumber(){return groupNumber;}
bool cell::get_isEntrance(){return isEntrance;}
bool cell::get_isExit(){return isExit;}
std::uint8_t cell::get_walls(){return walls;}
std::pair<int,int> cell::get_coords(){return coords;}

void cell::set_groupNumber(int GN){groupNumber = GN;}

void cell::removeWallNorth(){walls = walls & 0b00000111;}
void cell::removeWallEast(){walls = walls & 0b00001011;}
void cell::removeWallSouth(){walls = walls & 0b00001101;}
void cell::removeWallWest(){walls = walls & 0b00001110;}

void cell::makeEnter(){isEntrance = true;cell::removeWallWest();}
void cell::makeExit(){isExit = true;cell::removeWallEast();}