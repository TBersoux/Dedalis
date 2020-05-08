#include "window.h"
#include "ui_window_saved.h"

//METHODS
window::window(QWidget *parent) : QWidget(parent),
                                  ui(new Ui::window)
{
    ui->setupUi(this);
    setWindowTitle("Dedalis");
    ui->MAX_X_edit->setText(QString::number(100));
    ui->MAX_Y_edit->setText(QString::number(100));
    window_x = 100;
    window_y = 100;

    ui->loading_text->setVisible(false);
}

window::~window()
{
    delete ui;
}

int window::get_window_x() { return window_x; }
int window::get_window_y() { return window_y; }

void window::set_window_x(int x) { window::window_x = x; }
void window::set_window_y(int y) { window::window_y = y; }

std::vector<std::vector<uint8_t>> window::build()
{

    clock_t t1, t2;
    t1 = clock();
    maze aMaze(window_x, window_y);
    aMaze.build();

    t2 = clock();
    float diff((float)t2 - (float)t1);
    float seconds = ((float)((int)((diff / CLOCKS_PER_SEC) * 100))) / 100;
    ui->time->setText(QString::number(seconds));

    return aMaze.get_mazeMap();
}

void window::draw(std::vector<std::vector<uint8_t>> mapToDraw)
{
    QPen pen(Qt::black, 3);
    int BOXSIDE = 10;
    scene.clear();
    ui->graphicsView->setScene(&scene);
    ui->graphicsView->centerOn(10, 0);
    ui->graphicsView->show();

    for (int y = 0; y < window_y; y++)
    {
        for (int x = 0; x < window_x; x++)
        {
            int toDraw = mapToDraw[x][y];
            int drawingX = (x + 1) * BOXSIDE;
            int drawingY = (y + 1) * BOXSIDE;
            switch (toDraw)
            {
            case 0:
                break;
            case 1:
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                break;
            case 2:
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 3:
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 4:
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 5:
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 6:
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 7:
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                break;
            case 8:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                break;
            case 9:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                break;
            case 10:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 11:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE);
                break;
            case 12:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 13:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                break;
            case 14:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                break;
            case 15:
                scene.addLine(drawingX, drawingY, drawingX + BOXSIDE, drawingY, pen);
                scene.addLine(drawingX + BOXSIDE, drawingY, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY + BOXSIDE, drawingX + BOXSIDE, drawingY + BOXSIDE, pen);
                scene.addLine(drawingX, drawingY, drawingX, drawingY + BOXSIDE, pen);
                break;

            default:
                std::cout << "ERROR WHILE DRAWING" << std::endl;
                break;
            }
        }
    }
}

//SLOTS

void window::on_boutonGen_clicked()
{
    ui->loading_text->setVisible(true);
    QCoreApplication::processEvents();

    std::vector<std::vector<uint8_t>> aMazeMap = window::build();
    ui->loading_text->setVisible(false);
    window::draw(aMazeMap);
}

void window::on_MAX_X_edit_textChanged(QString n) { set_window_x(n.toInt()); }
void window::on_MAX_Y_edit_textChanged(QString n) { set_window_y(n.toInt()); }
