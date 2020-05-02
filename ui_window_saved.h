/********************************************************************************
** Form generated from reading UI file 'window.ui'
**
** Created by: Qt User Interface Compiler version 5.9.5
**
** Saved version - Change manually if needed
********************************************************************************/

#ifndef UI_WINDOW_H
#define UI_WINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_window
{
public:
    QVBoxLayout *verticalLayout;
    QGraphicsView *graphicsView;
    QHBoxLayout *horizontalLayout;
    QLineEdit *MAX_X_edit;
    QLineEdit *MAX_Y_edit;
    QPushButton *boutonGen;
    QLabel *loading_text;
    QSpacerItem *horizontalSpacer;
    QLabel *label;
    QLabel *time;

    void setupUi(QWidget *window)
    {
        if (window->objectName().isEmpty())
            window->setObjectName(QStringLiteral("window"));
        window->resize(1024, 768);
        verticalLayout = new QVBoxLayout(window);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        graphicsView = new QGraphicsView(window);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));

        verticalLayout->addWidget(graphicsView);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setSizeConstraint(QLayout::SetNoConstraint);
        MAX_X_edit = new QLineEdit(window);
        MAX_X_edit->setObjectName(QStringLiteral("MAX_X_edit"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MAX_X_edit->sizePolicy().hasHeightForWidth());
        MAX_X_edit->setSizePolicy(sizePolicy);
        MAX_X_edit->setMinimumSize(QSize(70, 23));
        MAX_X_edit->setMaximumSize(QSize(70, 23));
        MAX_X_edit->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(MAX_X_edit);

        MAX_Y_edit = new QLineEdit(window);
        MAX_Y_edit->setObjectName(QStringLiteral("MAX_Y_edit"));
        sizePolicy.setHeightForWidth(MAX_Y_edit->sizePolicy().hasHeightForWidth());
        MAX_Y_edit->setSizePolicy(sizePolicy);
        MAX_Y_edit->setMinimumSize(QSize(70, 23));
        MAX_Y_edit->setMaximumSize(QSize(70, 23));
        MAX_Y_edit->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(MAX_Y_edit);

        boutonGen = new QPushButton(window);
        boutonGen->setObjectName(QStringLiteral("boutonGen"));
        sizePolicy.setHeightForWidth(boutonGen->sizePolicy().hasHeightForWidth());
        boutonGen->setSizePolicy(sizePolicy);
        boutonGen->setMinimumSize(QSize(80, 23));

        horizontalLayout->addWidget(boutonGen);

        loading_text = new QLabel(window);
        loading_text->setObjectName(QStringLiteral("loading_text"));
        loading_text->setEnabled(true);

        horizontalLayout->addWidget(loading_text);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        label = new QLabel(window);
        label->setObjectName(QStringLiteral("label"));
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMinimumSize(QSize(90, 20));
        label->setMaximumSize(QSize(90, 20));

        horizontalLayout->addWidget(label);

        time = new QLabel(window);
        time->setObjectName(QStringLiteral("time"));
        sizePolicy.setHeightForWidth(time->sizePolicy().hasHeightForWidth());
        time->setSizePolicy(sizePolicy);
        time->setMinimumSize(QSize(60, 15));
        time->setMaximumSize(QSize(60, 15));
        QFont font;
        font.setBold(true);
        font.setWeight(75);
        time->setFont(font);
        time->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(time);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(window);

        QMetaObject::connectSlotsByName(window);
    } // setupUi

    void retranslateUi(QWidget *window)
    {
        window->setWindowTitle(QApplication::translate("window", "window", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        MAX_X_edit->setToolTip(QApplication::translate("window", "<html><head/><body><p>Set width of maze</p></body></html>", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_WHATSTHIS
        MAX_X_edit->setWhatsThis(QApplication::translate("window", "<html><head/><body><p><br/></p></body></html>", Q_NULLPTR));
#endif // QT_NO_WHATSTHIS
        MAX_X_edit->setText(QApplication::translate("window", "100", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        MAX_Y_edit->setToolTip(QApplication::translate("window", "<html><head/><body><p>Set height of maze</p></body></html>", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        MAX_Y_edit->setText(QApplication::translate("window", "100", Q_NULLPTR));
        boutonGen->setText(QApplication::translate("window", "Generate", Q_NULLPTR));
        loading_text->setText(QApplication::translate("window", "Please wait while generating ...", Q_NULLPTR));
        label->setText(QApplication::translate("window", "Gen. time (s) :", Q_NULLPTR));
        time->setText(QApplication::translate("window", "0", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class window: public Ui_window {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WINDOW_H
