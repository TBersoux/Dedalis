#include <string>
#include "cell.hpp"
#include "maze.hpp"
#include <time.h>
#include <iostream>
#include <QApplication>
#include "window.h"
#include <QWidget>

#include <fstream>

using namespace std;

//Used to test things
void draw(int toDraw)
{
    switch (toDraw)
    {
    case 1:
        cout << "|  ";
        break;
    case 2:
        cout << " _ ";
        break;
    case 3:
        cout << "|_ ";
        break;
    case 4:
        cout << "|  ";
        break;
    case 5:
        cout << "| |";
        break;
    case 6:
        cout << " _|";
        break;
    case 7:
        cout << "|_|";
        break;
    case 8:
        cout << " - ";
        break;
    case 9:
        cout << "|- ";
        break;
    case 10:
        cout << " = ";
        break;
    case 11:
        cout << "|= ";
        break;
    case 12:
        cout << " -|";
        break;
    case 13:
        cout << "|-|";
        break;
    case 14:
        cout << " =|";
        break;
    case 15:
        cout << "|=|";
        break;

    default:
        cout << "   ";
        break;
    }
}

string mode = "gui";
int main_x = 100;
int main_y = 100;

int main(int argc, char *argv[])
{
    if (argc > 2)
    {
        main_x = atol(argv[1]);
        main_y = atol(argv[2]);
        mode = "manual";
    }
    

    if (mode == "gui")
    {
        QApplication app(argc, argv);

        window mainWindow;
        mainWindow.show();

        return app.exec();
    }
    else
    {

        clock_t t1, t2;
        t1 = clock();

        maze aMaze(main_x, main_y);
        aMaze.build();
        auto carte = aMaze.get_mazeMap();

        t2 = clock();
        float diff((float)t2 - (float)t1);
        float seconds = diff / CLOCKS_PER_SEC;
        cout << "Seconds to build : " << seconds << endl;
        ofstream out;
        out.open("tests.txt", ios::app);
        out << "Temps : " << seconds << endl;
        out.close();

        //Uncomment this to see a drawing on the maze in stdout (But you should use gui mode)

        /* for (int y = 0; y < main_y; y++)
       {
           for (int x = 0; x < main_x; x++)
           {
               cout << draw((int)carte[x][y]);
           }
           cout << endl;
       }*/
    }
}
