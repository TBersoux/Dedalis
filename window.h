#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>
#include <QPen>
#include "maze.hpp"
#include <iostream>
#include <QGraphicsScene>
#include <time.h>

namespace Ui {
class window;
}

class window : public QWidget
{
    Q_OBJECT

public:
    explicit window(QWidget *parent = 0);
    ~window();


    int get_window_x();
    int get_window_y();
    void set_window_x(int);
    void set_window_y(int);

    void draw(std::vector<std::vector<uint8_t>>);



public slots:

    void on_boutonGen_clicked();
    void on_MAX_X_edit_textChanged(QString);
    void on_MAX_Y_edit_textChanged(QString);

private:
    Ui::window *ui;
    int window_x;
    int window_y;
    QGraphicsScene scene;

};

#endif // WINDOW_H
