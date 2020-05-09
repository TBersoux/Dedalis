#include <string>
#include "cell.hpp"
#include "maze.hpp"
#include <QApplication>
#include "window.h"
#include <QWidget>

int main(int argc, char *argv[])
{
    QApplication app(argc,argv);

    window mainWindow;
    mainWindow.show();

    return app.exec();
}
