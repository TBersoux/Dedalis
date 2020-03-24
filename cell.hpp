//cell.hpp
//Creation : 09/03/20

#ifndef cell_hpp
#define cell_hpp

#include <cstdint>


struct coord //A pair of int, x and y
{
    int x;
    int y;
};

class cell //a cell is a simple 2D object with 4 walls.
{
    public:
        //Constructor
        cell(int, int , int Y);


        //Destructor
        ~cell();

        //Getters

        int get_groupNumber();
        bool get_isEntrance();
        bool get_isExit();
        std::uint8_t get_walls();
        coord get_coords();

        //Setter
        void set_groupNumber(int);

        //Wall removers
        void removeWallNorth();
        void removeWallEast();
        void removeWallSouth();
        void removeWallWest();

        //Make that cell the entrance
        void makeEnter();

        //Make that cell the exit
        void makeExit();






    private : 
        int groupNumber; //Start at 0
        bool isEntrance; //Entrance of the maze
        bool isExit; //Exit of the maze

        int coordX; 
        int coordY; 

        coord coords;

        //State of the walls are stocked as a byte : Each bit from the 4 lasts refer to a wall, in this order : North,East,South,West
        //A wall at "1" is up
        std::uint8_t walls= 0b00001111;


};

#endif 