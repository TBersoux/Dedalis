//settings.h
//Creation : 21/03/20

//Used for constants and other useful global stuff

#include <iostream>

using namespace std;

#ifndef settings_hpp
#define settings_hpp

extern int MAX_X; //Number of columns of the maze
extern int MAX_Y; //Number of rows of the maze


//Override the default values of the global variables
void change_settings();

#endif