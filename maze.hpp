//maze.hpp
//Creation : 20/03/20

#ifndef maze_hpp
#define maze_hpp

#include "cell.hpp"
#include <vector>
#include <set>

class maze //A maze is a group of cells, including one enter and one exit

{
    public:
        //Constructors
        maze(int, int);

        //Destructor
        ~maze();

        //Getters
        std::vector<std::vector<uint8_t>> get_mazeMap(); 
        std::vector<std::vector<cell>> get_mazeCore(); // should not be used
        int get_MAX_X();
        int get_MAX_Y();

        //Setters
        void set_MAX_X(int);
        void set_MAX_Y(int);


        //Updates all the cells' groupnumbers depending of the chosen cells when calling maze.build()
        //See maze.build for details
        void updateGroups(int, int);

        //Check for surrounded cells, and removes them
        void removeSurrounded();

        /* Rules to build the maze :
        #1 A wall on the edge of a maze cannot be destroyed
        #2 wall separating two cells with the same group number cannot be destroyed 
        */

        //Build the maze following the two rules stated above (see maze.cpp for more details)
        void build();


    private:
    std::set<std::pair<int,int>> unreachableCoords; //Used to build the maze
    std::vector<std::vector<cell>> mazeCore; //The maze itself : cells in a 2D Array. Empty when built.
    std::vector<std::vector<uint8_t>> mazeMap;  //Map of the maze, using the walls (represented as bytes)
    int MAX_X;
    int MAX_Y;
};


#endif 
