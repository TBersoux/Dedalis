#include <string>
#include "cell.hpp"
#include "maze.hpp"
#include "settings.h"

using namespace std;

void draw(int toDraw)
{
    switch (toDraw)
    {
    case 1:
        cout <<"|  ";
        break;
    case 2:
        cout <<" _ ";
        break;
    case 3:
        cout <<"|_ ";
        break;
    case 4:
        cout <<"|  ";
        break;
    case 5:
        cout <<"| |";
        break;
    case 6:
        cout <<" _|";
        break;
    case 7:
        cout <<"|_|";
        break;
    case 8:
        cout <<" - ";
        break;
    case 9:
        cout <<"|- ";
        break;
    case 10:
        cout <<" = ";
        break;
    case 11:
        cout <<"|= ";
        break;
    case 12:
        cout <<" -|";
        break;
    case 13:
        cout <<"|-|";
        break;
    case 14:
        cout <<" =|";
        break;
    case 15:
        cout <<"|=|";
        break;
    
    default:
    cout << "   ";
        break;
    }
    
}

int main(void)
{

    maze laby;
    laby.build();
    auto carte = laby.get_mazeMap();

    for (int y = 0; y < MAX_Y; y++)
    {
        break;
        for (int x = 0; x < MAX_X; x++)
        {
            draw(int(carte[x][y]));
        }
        cout << endl;
    }
    

    /*for (size_t y = 0; y < MAX_Y; y++)
    {
        cout << endl;
        for (size_t x = 0; x < MAX_X; x++)
        {
            cout << test[x][y].get_groupNumber() << " ";
        }
        
    }*/
    cout << "sortie" <<endl;
    return 0;
    }