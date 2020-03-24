#include <string>
#include "cell.hpp"
#include "maze.hpp"
#include "settings.h"

using namespace std;

int main(void)
{

    maze laby;
    laby.build();

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