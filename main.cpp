#include <string>
#include "cell.hpp"
#include "maze.hpp"
#include "settings.h"
#include <time.h>

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
    clock_t t1,t2;
    t1=clock();

    maze laby;
    laby.build();
    auto carte = laby.get_mazeMap();

    for (int y = 0; y < MAX_Y; y++)
    {
        //!! : POUR TESTER enlever break;
        break;
        for (int x = 0; x < MAX_X; x++)
        {
            draw(int(carte[x][y]));
        }
        cout << endl;
    }
    
    t2=clock();
    float diff ((float)t2-(float)t1);
    float seconds = diff / CLOCKS_PER_SEC;
    cout << "sortie en sec :" << seconds <<endl;
    return 0;
    }