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
#include <QtWidgets/QListView>
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
    QHBoxLayout *horizontalLayout_13;
    QTabWidget *tabWidget_2;
    QWidget *tabDecisionTree;
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
    QWidget *tabBN;
    QHBoxLayout *horizontalLayout_10;
    QHBoxLayout *horizontalLayout_11;
    QTabWidget *tabWidget_3;
    QWidget *tabBNData;
    QHBoxLayout *horizontalLayout_9;
    QVBoxLayout *verticalLayout_8;
    QLabel *label_15;
    QPushButton *pushButtonDir;
    QLabel *label_16;
    QListView *listView;
    QLabel *label_14;
    QTableView *tableView_2;
    QSpacerItem *verticalSpacer_5;
    QWidget *tab_3;
    QHBoxLayout *horizontalLayout_12;
    QVBoxLayout *verticalLayout_10;
    QLabel *label_21;
    QPushButton *pushButtongenerateBN;
    QLabel *label_17;
    QPushButton *pushButtonQuery;
    QLabel *label_18;
    QLabel *labelvar;
    QLabel *label_19;
    QLabel *labelcond;
    QPushButton *pushButtonInfer;
    QLabel *label_20;
    QLineEdit *lineEditprob;
    QSpacerItem *verticalSpacer_6;
    QVBoxLayout *verticalLayout_9;
    Canvas *graphicsViewBN;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1196, 638);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout_13 = new QHBoxLayout(centralwidget);
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        tabWidget_2 = new QTabWidget(centralwidget);
        tabWidget_2->setObjectName(QString::fromUtf8("tabWidget_2"));
        tabDecisionTree = new QWidget();
        tabDecisionTree->setObjectName(QString::fromUtf8("tabDecisionTree"));
        horizontalLayout_8 = new QHBoxLayout(tabDecisionTree);
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        MainFrame = new QHBoxLayout();
        MainFrame->setObjectName(QString::fromUtf8("MainFrame"));
        MainFrame->setSizeConstraint(QLayout::SetMaximumSize);
        tabWidget = new QTabWidget(tabDecisionTree);
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
        tableViewTrain->setFrameShadow(QFrame::Plain);
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
        tableViewTest->setFrameShadow(QFrame::Plain);
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

        mainSep2 = new QFrame(tabDecisionTree);
        mainSep2->setObjectName(QString::fromUtf8("mainSep2"));
        mainSep2->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        mainSep2->setFrameShadow(QFrame::Plain);
        mainSep2->setLineWidth(2);
        mainSep2->setFrameShape(QFrame::VLine);

        MainFrame->addWidget(mainSep2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        scrollArea = new QScrollArea(tabDecisionTree);
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
        canvas->setGeometry(QRect(0, 0, 551, 507));
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

        mainSep1 = new QFrame(tabDecisionTree);
        mainSep1->setObjectName(QString::fromUtf8("mainSep1"));
        mainSep1->setFrameShape(QFrame::VLine);
        mainSep1->setFrameShadow(QFrame::Sunken);

        MainFrame->addWidget(mainSep1);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_5 = new QLabel(tabDecisionTree);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout_2->addWidget(label_5);

        horizontalSpacer_6 = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_6);

        horizontalLayout_2->setStretch(1, 1);

        verticalLayout_2->addLayout(horizontalLayout_2);

        line_6 = new QFrame(tabDecisionTree);
        line_6->setObjectName(QString::fromUtf8("line_6"));
        line_6->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        line_6->setFrameShadow(QFrame::Plain);
        line_6->setLineWidth(2);
        line_6->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line_6);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        lineRunTime = new QLineEdit(tabDecisionTree);
        lineRunTime->setObjectName(QString::fromUtf8("lineRunTime"));
        lineRunTime->setReadOnly(true);

        gridLayout_2->addWidget(lineRunTime, 0, 1, 1, 1);

        labelRunTime = new QLabel(tabDecisionTree);
        labelRunTime->setObjectName(QString::fromUtf8("labelRunTime"));

        gridLayout_2->addWidget(labelRunTime, 0, 0, 1, 1);


        verticalLayout_2->addLayout(gridLayout_2);

        line_3 = new QFrame(tabDecisionTree);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setStyleSheet(QString::fromUtf8("color: rgb(202, 202, 202);"));
        line_3->setFrameShadow(QFrame::Plain);
        line_3->setLineWidth(2);
        line_3->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line_3);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_4 = new QLabel(tabDecisionTree);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_5->addWidget(label_4);

        horizontalSpacer_4 = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_4);


        verticalLayout_2->addLayout(horizontalLayout_5);

        line = new QFrame(tabDecisionTree);
        line->setObjectName(QString::fromUtf8("line"));
        line->setAutoFillBackground(false);
        line->setStyleSheet(QString::fromUtf8("color: rgb(202, 202, 202);"));
        line->setFrameShadow(QFrame::Plain);
        line->setLineWidth(2);
        line->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(tabDecisionTree);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        lineEval = new QLineEdit(tabDecisionTree);
        lineEval->setObjectName(QString::fromUtf8("lineEval"));
        lineEval->setReadOnly(true);

        gridLayout->addWidget(lineEval, 1, 1, 1, 1);

        label_2 = new QLabel(tabDecisionTree);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        lineOther = new QLineEdit(tabDecisionTree);
        lineOther->setObjectName(QString::fromUtf8("lineOther"));
        lineOther->setReadOnly(true);

        gridLayout->addWidget(lineOther, 2, 1, 1, 1);

        lineEvidence = new QLineEdit(tabDecisionTree);
        lineEvidence->setObjectName(QString::fromUtf8("lineEvidence"));
        lineEvidence->setEnabled(true);
        lineEvidence->setReadOnly(true);

        gridLayout->addWidget(lineEvidence, 0, 1, 1, 1);

        label_3 = new QLabel(tabDecisionTree);
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

        line_5 = new QFrame(tabDecisionTree);
        line_5->setObjectName(QString::fromUtf8("line_5"));
        line_5->setStyleSheet(QString::fromUtf8("color: rgb(203, 203, 203);"));
        line_5->setFrameShadow(QFrame::Plain);
        line_5->setLineWidth(2);
        line_5->setFrameShape(QFrame::HLine);

        verticalLayout_2->addWidget(line_5);

        label_11 = new QLabel(tabDecisionTree);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        verticalLayout_2->addWidget(label_11);

        label_12 = new QLabel(tabDecisionTree);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        verticalLayout_2->addWidget(label_12);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        lineEditacc = new QLineEdit(tabDecisionTree);
        lineEditacc->setObjectName(QString::fromUtf8("lineEditacc"));
        lineEditacc->setReadOnly(true);

        horizontalLayout_3->addWidget(lineEditacc);

        label_13 = new QLabel(tabDecisionTree);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        horizontalLayout_3->addWidget(label_13);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_7);


        verticalLayout_2->addLayout(horizontalLayout_3);

        tableView = new QTableView(tabDecisionTree);
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

        tabWidget_2->addTab(tabDecisionTree, QString());
        tabBN = new QWidget();
        tabBN->setObjectName(QString::fromUtf8("tabBN"));
        horizontalLayout_10 = new QHBoxLayout(tabBN);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        tabWidget_3 = new QTabWidget(tabBN);
        tabWidget_3->setObjectName(QString::fromUtf8("tabWidget_3"));
        sizePolicy1.setHeightForWidth(tabWidget_3->sizePolicy().hasHeightForWidth());
        tabWidget_3->setSizePolicy(sizePolicy1);
        tabWidget_3->setMaximumSize(QSize(300, 16777215));
        tabBNData = new QWidget();
        tabBNData->setObjectName(QString::fromUtf8("tabBNData"));
        horizontalLayout_9 = new QHBoxLayout(tabBNData);
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        verticalLayout_8 = new QVBoxLayout();
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        label_15 = new QLabel(tabBNData);
        label_15->setObjectName(QString::fromUtf8("label_15"));

        verticalLayout_8->addWidget(label_15);

        pushButtonDir = new QPushButton(tabBNData);
        pushButtonDir->setObjectName(QString::fromUtf8("pushButtonDir"));

        verticalLayout_8->addWidget(pushButtonDir, 0, Qt::AlignLeft);

        label_16 = new QLabel(tabBNData);
        label_16->setObjectName(QString::fromUtf8("label_16"));

        verticalLayout_8->addWidget(label_16);

        listView = new QListView(tabBNData);
        listView->setObjectName(QString::fromUtf8("listView"));
        sizePolicy1.setHeightForWidth(listView->sizePolicy().hasHeightForWidth());
        listView->setSizePolicy(sizePolicy1);
        listView->setMaximumSize(QSize(220, 16777215));

        verticalLayout_8->addWidget(listView);

        label_14 = new QLabel(tabBNData);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        verticalLayout_8->addWidget(label_14);

        tableView_2 = new QTableView(tabBNData);
        tableView_2->setObjectName(QString::fromUtf8("tableView_2"));
        sizePolicy1.setHeightForWidth(tableView_2->sizePolicy().hasHeightForWidth());
        tableView_2->setSizePolicy(sizePolicy1);
        tableView_2->setMaximumSize(QSize(220, 16777215));
        tableView_2->horizontalHeader()->setMinimumSectionSize(10);
        tableView_2->horizontalHeader()->setDefaultSectionSize(40);
        tableView_2->verticalHeader()->setMinimumSectionSize(10);
        tableView_2->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_8->addWidget(tableView_2);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_8->addItem(verticalSpacer_5);


        horizontalLayout_9->addLayout(verticalLayout_8);

        tabWidget_3->addTab(tabBNData, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        horizontalLayout_12 = new QHBoxLayout(tab_3);
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        verticalLayout_10 = new QVBoxLayout();
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        label_21 = new QLabel(tab_3);
        label_21->setObjectName(QString::fromUtf8("label_21"));

        verticalLayout_10->addWidget(label_21);

        pushButtongenerateBN = new QPushButton(tab_3);
        pushButtongenerateBN->setObjectName(QString::fromUtf8("pushButtongenerateBN"));

        verticalLayout_10->addWidget(pushButtongenerateBN, 0, Qt::AlignLeft);

        label_17 = new QLabel(tab_3);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setTextFormat(Qt::AutoText);

        verticalLayout_10->addWidget(label_17);

        pushButtonQuery = new QPushButton(tab_3);
        pushButtonQuery->setObjectName(QString::fromUtf8("pushButtonQuery"));

        verticalLayout_10->addWidget(pushButtonQuery, 0, Qt::AlignLeft);

        label_18 = new QLabel(tab_3);
        label_18->setObjectName(QString::fromUtf8("label_18"));

        verticalLayout_10->addWidget(label_18);

        labelvar = new QLabel(tab_3);
        labelvar->setObjectName(QString::fromUtf8("labelvar"));
        labelvar->setStyleSheet(QString::fromUtf8("border-color: rgb(81, 81, 81);"));
        labelvar->setFrameShape(QFrame::Panel);
        labelvar->setFrameShadow(QFrame::Sunken);

        verticalLayout_10->addWidget(labelvar);

        label_19 = new QLabel(tab_3);
        label_19->setObjectName(QString::fromUtf8("label_19"));

        verticalLayout_10->addWidget(label_19);

        labelcond = new QLabel(tab_3);
        labelcond->setObjectName(QString::fromUtf8("labelcond"));
        labelcond->setFrameShape(QFrame::Panel);
        labelcond->setFrameShadow(QFrame::Sunken);

        verticalLayout_10->addWidget(labelcond);

        pushButtonInfer = new QPushButton(tab_3);
        pushButtonInfer->setObjectName(QString::fromUtf8("pushButtonInfer"));

        verticalLayout_10->addWidget(pushButtonInfer, 0, Qt::AlignLeft);

        label_20 = new QLabel(tab_3);
        label_20->setObjectName(QString::fromUtf8("label_20"));

        verticalLayout_10->addWidget(label_20);

        lineEditprob = new QLineEdit(tab_3);
        lineEditprob->setObjectName(QString::fromUtf8("lineEditprob"));
        lineEditprob->setReadOnly(true);

        verticalLayout_10->addWidget(lineEditprob);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_10->addItem(verticalSpacer_6);


        horizontalLayout_12->addLayout(verticalLayout_10);

        tabWidget_3->addTab(tab_3, QString());

        horizontalLayout_11->addWidget(tabWidget_3);

        verticalLayout_9 = new QVBoxLayout();
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        graphicsViewBN = new Canvas(tabBN);
        graphicsViewBN->setObjectName(QString::fromUtf8("graphicsViewBN"));

        verticalLayout_9->addWidget(graphicsViewBN);


        horizontalLayout_11->addLayout(verticalLayout_9);


        horizontalLayout_10->addLayout(horizontalLayout_11);

        tabWidget_2->addTab(tabBN, QString());

        horizontalLayout_13->addWidget(tabWidget_2);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1196, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        tabWidget_2->setCurrentIndex(0);
        tabWidget->setCurrentIndex(0);
        comboTreeType->setCurrentIndex(0);
        tabWidget_3->setCurrentIndex(1);


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
        tabWidget_2->setTabText(tabWidget_2->indexOf(tabDecisionTree), QCoreApplication::translate("MainWindow", "\345\206\263\347\255\226\346\240\221", nullptr));
        label_15->setText(QCoreApplication::translate("MainWindow", "\346\226\207\344\273\266\346\225\260\346\215\256", nullptr));
        pushButtonDir->setText(QCoreApplication::translate("MainWindow", "\346\211\223\345\274\200\346\226\207\344\273\266\345\244\271", nullptr));
        label_16->setText(QCoreApplication::translate("MainWindow", "\346\226\207\344\273\266\345\244\271\345\206\205\345\256\271", nullptr));
        label_14->setText(QCoreApplication::translate("MainWindow", "\350\264\235\345\217\266\346\226\257\347\275\221\347\273\234\346\225\260\346\215\256", nullptr));
        tabWidget_3->setTabText(tabWidget_3->indexOf(tabBNData), QCoreApplication::translate("MainWindow", "\346\225\260\346\215\256", nullptr));
        label_21->setText(QCoreApplication::translate("MainWindow", "\347\224\237\346\210\220\350\264\235\345\217\266\346\226\257\347\275\221\347\273\234", nullptr));
        pushButtongenerateBN->setText(QCoreApplication::translate("MainWindow", "\347\224\237\346\210\220", nullptr));
        label_17->setText(QCoreApplication::translate("MainWindow", "\346\237\245\350\257\242", nullptr));
        pushButtonQuery->setText(QCoreApplication::translate("MainWindow", "\346\211\223\345\274\200\346\237\245\350\257\242", nullptr));
        label_18->setText(QCoreApplication::translate("MainWindow", "Variable", nullptr));
        labelvar->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label_19->setText(QCoreApplication::translate("MainWindow", "Condition", nullptr));
        labelcond->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        pushButtonInfer->setText(QCoreApplication::translate("MainWindow", "\350\277\220\350\241\214", nullptr));
        label_20->setText(QCoreApplication::translate("MainWindow", "\345\220\216\351\252\214\346\246\202\347\216\207", nullptr));
        tabWidget_3->setTabText(tabWidget_3->indexOf(tab_3), QCoreApplication::translate("MainWindow", "\350\277\220\350\241\214", nullptr));
        tabWidget_2->setTabText(tabWidget_2->indexOf(tabBN), QCoreApplication::translate("MainWindow", "\350\264\235\345\217\266\346\226\257\347\275\221\347\273\234", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_H
