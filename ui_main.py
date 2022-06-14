/********************************************************************************
** Form generated from reading UI file 'main.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAIN_H
#define UI_MAIN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableView>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "module/canvas"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout_8;
    QVBoxLayout *verticalLayout_6;
    QHBoxLayout *MainFrame;
    QTabWidget *tabWidget;
    QWidget *tabData;
    QHBoxLayout *horizontalLayout_4;
    QVBoxLayout *verticalLayout_3;
    QFrame *line_4;
    QLabel *label_6;
    QHBoxLayout *horizontalLayout_6;
    QPushButton *openFileButton;
    QSpacerItem *horizontalSpacer_5;
    QTableView *tableViewTrain;
    QLabel *label_8;
    QFrame *line_2;
    QPushButton *pushButtonTest;
    QTableView *tableViewTest;
    QSpacerItem *verticalSpacer_2;
    QWidget *tabSetting;
    QVBoxLayout *verticalLayout_5;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_7;
    QComboBox *comboTreeType;
    QSpacerItem *verticalSpacer_3;
    QWidget *tab;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_7;
    QLabel *label_9;
    QPushButton *pushButtonBuildTree;
    QLabel *label_10;
    QPushButton *pushButtonRunTest;
    QSpacerItem *verticalSpacer_4;
    QFrame *mainSep2;
    QVBoxLayout *verticalLayout;
    QScrollArea *scrollArea;
    QWidget *canvas;
    QHBoxLayout *horizontalLayout_7;
    Canvas *graphicsView;
    QFrame *mainSep1;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_5;
    QSpacerItem *horizontalSpacer_6;
    QFrame *line_6;
    QGridLayout *gridLayout_2;
    QLineEdit *lineRunTime;
    QLabel *labelRunTime;
    QFrame *line_3;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_4;
    QSpacerItem *horizontalSpacer_4;
    QFrame *line;
    QGridLayout *gridLayout;
    QLabel *label;
    QLineEdit *lineEval;
    QLabel *label_2;
    QLineEdit *lineOther;
    QLineEdit *lineEvidence;
    QLabel *label_3;
    QSpacerItem *horizontalSpacer;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *horizontalSpacer_3;
    QFrame *line_5;
    QLabel *label_11;
    QLabel *label_12;
    QHBoxLayout *horizontalLayout_3;
    QLineEdit *lineEditacc;
    QLabel *label_13;
    QSpacerItem *horizontalSpacer_7;
    QTableView *tableView;
    QSpacerItem *verticalSpacer;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1089, 850);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout_8 = new QHBoxLayout(centralwidget);
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        MainFrame = new QHBoxLayout();
        MainFrame->setObjectName(QString::fromUtf8("MainFrame"));
        MainFrame->setSizeConstraint(QLayout::SetMaximumSize);
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::Maximum, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy1);
        tabWidget->setMinimumSize(QSize(0, 0));
        tabWidget->setMaximumSize(QSize(300, 10000));
        tabWidget->setTabletTracking(false);
        tabWidget->setElideMode(Qt::ElideMiddle);
        tabData = new QWidget();
        tabData->setObjectName(QString::fromUtf8("tabData"));
        horizontalLayout_4 = new QHBoxLayout(tabData);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(5, -1, 5, -1);
        line_4 = new QFrame(tabData);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        line_4->setFrameShadow(QFrame::Plain);
        line_4->setFrameShape(QFrame::HLine);

        verticalLayout_3->addWidget(line_4);

        label_6 = new QLabel(tabData);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        verticalLayout_3->addWidget(label_6);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        openFileButton = new QPushButton(tabData);
        openFileButton->setObjectName(QString::fromUtf8("openFileButton"));

        horizontalLayout_6->addWidget(openFileButton);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_5);


        verticalLayout_3->addLayout(horizontalLayout_6);

        tableViewTrain = new QTableView(tabData);
        tableViewTrain->setObjectName(QString::fromUtf8("tableViewTrain"));
        sizePolicy1.setHeightForWidth(tableViewTrain->sizePolicy().hasHeightForWidth());
        tableViewTrain->setSizePolicy(sizePolicy1);
        tableViewTrain->setMinimumSize(QSize(0, 0));
        tableViewTrain->setMaximumSize(QSize(300, 16777215));
        tableViewTrain->setStyleSheet(QString::fromUtf8(""));
        tableViewTrain->setSizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored);
        tableViewTrain->horizontalHeader()->setMinimumSectionSize(10);
        tableViewTrain->horizontalHeader()->setDefaultSectionSize(40);
        tableViewTrain->verticalHeader()->setMinimumSectionSize(10);
        tableViewTrain->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_3->addWidget(tableViewTrain);

        label_8 = new QLabel(tabData);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        verticalLayout_3->addWidget(label_8);

        line_2 = new QFrame(tabData);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        line_2->setFrameShadow(QFrame::Plain);
        line_2->setFrameShape(QFrame::HLine);

        verticalLayout_3->addWidget(line_2);

        pushButtonTest = new QPushButton(tabData);
        pushButtonTest->setObjectName(QString::fromUtf8("pushButtonTest"));

        verticalLayout_3->addWidget(pushButtonTest, 0, Qt::AlignLeft);

        tableViewTest = new QTableView(tabData);
        tableViewTest->setObjectName(QString::fromUtf8("tableViewTest"));
        sizePolicy1.setHeightForWidth(tableViewTest->sizePolicy().hasHeightForWidth());
        tableViewTest->setSizePolicy(sizePolicy1);
        tableViewTest->setMaximumSize(QSize(300, 16777215));
        tableViewTest->horizontalHeader()->setMinimumSectionSize(10);
        tableViewTest->horizontalHeader()->setDefaultSectionSize(40);
        tableViewTest->verticalHeader()->setMinimumSectionSize(10);
        tableViewTest->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_3->addWidget(tableViewTest);

        verticalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Maximum);

        verticalLayout_3->addItem(verticalSpacer_2);


        horizontalLayout_4->addLayout(verticalLayout_3);

        tabWidget->addTab(tabData, QString());
        tabSetting = new QWidget();
        tabSetting->setObjectName(QString::fromUtf8("tabSetting"));
        verticalLayout_5 = new QVBoxLayout(tabSetting);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(5, 5, -1, -1);
        label_7 = new QLabel(tabSetting);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        verticalLayout_4->addWidget(label_7);

        comboTreeType = new QComboBox(tabSetting);
        comboTreeType->addItem(QString());
        comboTreeType->addItem(QString());
        comboTreeType->addItem(QString());
        comboTreeType->setObjectName(QString::fromUtf8("comboTreeType"));
        comboTreeType->setEditable(false);
        comboTreeType->setCurrentText(QString::fromUtf8("ID3"));

        verticalLayout_4->addWidget(comboTreeType);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_3);


        verticalLayout_5->addLayout(verticalLayout_4);

        tabWidget->addTab(tabSetting, QString());
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        horizontalLayout = new QHBoxLayout(tab);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        label_9 = new QLabel(tab);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        verticalLayout_7->addWidget(label_9);

        pushButtonBuildTree = new QPushButton(tab);
        pushButtonBuildTree->setObjectName(QString::fromUtf8("pushButtonBuildTree"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(pushButtonBuildTree->sizePolicy().hasHeightForWidth());
        pushButtonBuildTree->setSizePolicy(sizePolicy2);

        verticalLayout_7->addWidget(pushButtonBuildTree, 0, Qt::AlignLeft);

        label_10 = new QLabel(tab);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        verticalLayout_7->addWidget(label_10);

        pushButtonRunTest = new QPushButton(tab);
        pushButtonRunTest->setObjectName(QString::fromUtf8("pushButtonRunTest"));

        verticalLayout_7->addWidget(pushButtonRunTest, 0, Qt::AlignLeft);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_7->addItem(verticalSpacer_4);


        horizontalLayout->addLayout(verticalLayout_7);

        tabWidget->addTab(tab, QString());

        MainFrame->addWidget(tabWidget);

        mainSep2 = new QFrame(centralwidget);
        mainSep2->setObjectName(QString::fromUtf8("mainSep2"));
        mainSep2->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        mainSep2->setFrameShadow(QFrame::Plain);
        mainSep2->setLineWidth(2);
        mainSep2->setFrameShape(QFrame::VLine);

        MainFrame->addWidget(mainSep2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        scrollArea = new QScrollArea(centralwidget);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        QSizePolicy sizePolicy3(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy3.setHorizontalStretch(1);
        sizePolicy3.setVerticalStretch(1);
        sizePolicy3.setHeightForWidth(scrollArea->sizePolicy().hasHeightForWidth());
        scrollArea->setSizePolicy(sizePolicy3);
        scrollArea->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        scrollArea->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        scrollArea->setSizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored);
        scrollArea->setWidgetResizable(true);
        canvas = new QWidget();
        canvas->setObjectName(QString::fromUtf8("canvas"));
        canvas->setGeometry(QRect(0, 0, 468, 765));
        horizontalLayout_7 = new QHBoxLayout(canvas);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        graphicsView = new Canvas(canvas);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setSceneRect(QRectF(0, 0, 1000, 1000));
        graphicsView->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        graphicsView->setDragMode(QGraphicsView::NoDrag);

        horizontalLayout_7->addWidget(graphicsView);

        scrollArea->setWidget(canvas);

        verticalLayout->addWidget(scrollArea);


        MainFrame->addLayout(verticalLayout);

        mainSep1 = new QFrame(centralwidget);
        mainSep1->setObjectName(QString::fromUtf8("mainSep1"));
        mainSep1->setFrameShape(QFrame::VLine);
        mainSep1->setFrameShadow(QFrame::Sunken);

        MainFrame->addWidget(mainSep1);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_5 = new QLabel(centralwidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout_2->addWidget(label_5);

        horizontalSpacer_6 = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_6);

        horizontalLayout_2->setStretch(1, 1);

        verticalLayout_2->addLayout(horizontalLayout_2);

        line_6 = new QFrame(centralwidget);
        line_6->setObjectName(QString::fromUtf8("line_6"));
        line_6->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        line_6->setFrameShadow(QFrame::Plain);
        line_6->setLineWidth(2);
        line_6->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line_6);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        lineRunTime = new QLineEdit(centralwidget);
        lineRunTime->setObjectName(QString::fromUtf8("lineRunTime"));
        lineRunTime->setReadOnly(true);

        gridLayout_2->addWidget(lineRunTime, 0, 1, 1, 1);

        labelRunTime = new QLabel(centralwidget);
        labelRunTime->setObjectName(QString::fromUtf8("labelRunTime"));

        gridLayout_2->addWidget(labelRunTime, 0, 0, 1, 1);


        verticalLayout_2->addLayout(gridLayout_2);

        line_3 = new QFrame(centralwidget);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setStyleSheet(QString::fromUtf8("color: rgb(202, 202, 202);"));
        line_3->setFrameShadow(QFrame::Plain);
        line_3->setLineWidth(2);
        line_3->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line_3);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_5->addWidget(label_4);

        horizontalSpacer_4 = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_4);


        verticalLayout_2->addLayout(horizontalLayout_5);

        line = new QFrame(centralwidget);
        line->setObjectName(QString::fromUtf8("line"));
        line->setAutoFillBackground(false);
        line->setStyleSheet(QString::fromUtf8("color: rgb(202, 202, 202);"));
        line->setFrameShadow(QFrame::Plain);
        line->setLineWidth(2);
        line->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        lineEval = new QLineEdit(centralwidget);
        lineEval->setObjectName(QString::fromUtf8("lineEval"));
        lineEval->setReadOnly(true);

        gridLayout->addWidget(lineEval, 1, 1, 1, 1);

        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        lineOther = new QLineEdit(centralwidget);
        lineOther->setObjectName(QString::fromUtf8("lineOther"));
        lineOther->setReadOnly(true);

        gridLayout->addWidget(lineOther, 2, 1, 1, 1);

        lineEvidence = new QLineEdit(centralwidget);
        lineEvidence->setObjectName(QString::fromUtf8("lineEvidence"));
        lineEvidence->setEnabled(true);
        lineEvidence->setReadOnly(true);

        gridLayout->addWidget(lineEvidence, 0, 1, 1, 1);

        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 2, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 1, 2, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 2, 2, 1, 1);

        gridLayout->setColumnStretch(1, 1);

        verticalLayout_2->addLayout(gridLayout);

        line_5 = new QFrame(centralwidget);
        line_5->setObjectName(QString::fromUtf8("line_5"));
        line_5->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        line_5->setFrameShadow(QFrame::Plain);
        line_5->setLineWidth(2);
        line_5->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line_5);

        label_11 = new QLabel(centralwidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        verticalLayout_2->addWidget(label_11);

        label_12 = new QLabel(centralwidget);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        verticalLayout_2->addWidget(label_12);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        lineEditacc = new QLineEdit(centralwidget);
        lineEditacc->setObjectName(QString::fromUtf8("lineEditacc"));
        lineEditacc->setReadOnly(true);

        horizontalLayout_3->addWidget(lineEditacc);

        label_13 = new QLabel(centralwidget);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        horizontalLayout_3->addWidget(label_13);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_7);


        verticalLayout_2->addLayout(horizontalLayout_3);

        tableView = new QTableView(centralwidget);
        tableView->setObjectName(QString::fromUtf8("tableView"));
        tableView->horizontalHeader()->setMinimumSectionSize(10);
        tableView->horizontalHeader()->setDefaultSectionSize(40);
        tableView->verticalHeader()->setMinimumSectionSize(10);
        tableView->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_2->addWidget(tableView);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);


        MainFrame->addLayout(verticalLayout_2);

        MainFrame->setStretch(2, 2);

        verticalLayout_6->addLayout(MainFrame);


        horizontalLayout_8->addLayout(verticalLayout_6);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1089, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);
        comboTreeType->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "\350\256\255\347\273\203\346\225\260\346\215\256", nullptr));
        openFileButton->setText(QCoreApplication::translate("MainWindow", "\346\211\223\345\274\200\346\226\207\344\273\266", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "\346\265\213\350\257\225\346\225\260\346\215\256", nullptr));
        pushButtonTest->setText(QCoreApplication::translate("MainWindow", "\346\211\223\345\274\200\346\226\207\344\273\266", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tabData), QCoreApplication::translate("MainWindow", "\350\256\255\347\273\203\346\225\260\346\215\256", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "\345\206\263\347\255\226\346\240\221\347\261\273\345\236\213", nullptr));
        comboTreeType->setItemText(0, QCoreApplication::translate("MainWindow", "ID3", nullptr));
        comboTreeType->setItemText(1, QCoreApplication::translate("MainWindow", "C4.5", nullptr));
        comboTreeType->setItemText(2, QCoreApplication::translate("MainWindow", "CART", nullptr));

        tabWidget->setTabText(tabWidget->indexOf(tabSetting), QCoreApplication::translate("MainWindow", "\350\256\276\347\275\256", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "\345\273\272\347\253\213\345\206\263\347\255\226\346\240\221", nullptr));
        pushButtonBuildTree->setText(QCoreApplication::translate("MainWindow", "Build Tree", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "\350\277\220\350\241\214\346\265\213\350\257\225", nullptr));
        pushButtonRunTest->setText(QCoreApplication::translate("MainWindow", "Run test", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("MainWindow", "\350\277\220\350\241\214", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "\345\206\263\347\255\226\346\240\221\345\261\236\346\200\247", nullptr));
        labelRunTime->setText(QCoreApplication::translate("MainWindow", "\350\277\220\350\241\214\346\227\266\351\227\264", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "\350\212\202\347\202\271\345\261\236\346\200\247", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "\345\210\206\347\261\273\344\276\235\346\215\256", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "\350\257\204\344\273\267\346\214\207\346\240\207", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "\345\205\266\344\273\226", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "\351\242\204\346\265\213\347\273\223\346\236\234", nullptr));
        label_12->setText(QCoreApplication::translate("MainWindow", "\345\207\206\347\241\256\347\216\207", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "%", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_H
