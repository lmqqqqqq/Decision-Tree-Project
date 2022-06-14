# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QRectF,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

from module.canvas import Canvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_13 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabDecisionTree = QWidget()
        self.tabDecisionTree.setObjectName(u"tabDecisionTree")
        self.horizontalLayout_8 = QHBoxLayout(self.tabDecisionTree)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.MainFrame = QHBoxLayout()
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setSizeConstraint(QLayout.SetMaximumSize)
        self.tabWidget = QTabWidget(self.tabDecisionTree)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(300, 10000))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabData = QWidget()
        self.tabData.setObjectName(u"tabData")
        self.horizontalLayout_4 = QHBoxLayout(self.tabData)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.line_4 = QFrame(self.tabData)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_4)

        self.label_6 = QLabel(self.tabData)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.openFileButton = QPushButton(self.tabData)
        self.openFileButton.setObjectName(u"openFileButton")

        self.horizontalLayout_6.addWidget(self.openFileButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tableViewTrain = QTableView(self.tabData)
        self.tableViewTrain.setObjectName(u"tableViewTrain")
        sizePolicy1.setHeightForWidth(self.tableViewTrain.sizePolicy().hasHeightForWidth())
        self.tableViewTrain.setSizePolicy(sizePolicy1)
        self.tableViewTrain.setMinimumSize(QSize(0, 0))
        self.tableViewTrain.setMaximumSize(QSize(300, 16777215))
        self.tableViewTrain.setStyleSheet(u"")
        self.tableViewTrain.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableViewTrain.horizontalHeader().setMinimumSectionSize(10)
        self.tableViewTrain.horizontalHeader().setDefaultSectionSize(40)
        self.tableViewTrain.verticalHeader().setMinimumSectionSize(10)
        self.tableViewTrain.verticalHeader().setDefaultSectionSize(25)

        self.verticalLayout_3.addWidget(self.tableViewTrain)

        self.label_8 = QLabel(self.tabData)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.line_2 = QFrame(self.tabData)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_2)

        self.pushButtonTest = QPushButton(self.tabData)
        self.pushButtonTest.setObjectName(u"pushButtonTest")

        self.verticalLayout_3.addWidget(self.pushButtonTest, 0, Qt.AlignLeft)

        self.tableViewTest = QTableView(self.tabData)
        self.tableViewTest.setObjectName(u"tableViewTest")
        sizePolicy1.setHeightForWidth(self.tableViewTest.sizePolicy().hasHeightForWidth())
        self.tableViewTest.setSizePolicy(sizePolicy1)
        self.tableViewTest.setMaximumSize(QSize(300, 16777215))
        self.tableViewTest.horizontalHeader().setMinimumSectionSize(10)
        self.tableViewTest.horizontalHeader().setDefaultSectionSize(40)
        self.tableViewTest.verticalHeader().setMinimumSectionSize(10)
        self.tableViewTest.verticalHeader().setDefaultSectionSize(25)

        self.verticalLayout_3.addWidget(self.tableViewTest)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tabData, "")
        self.tabSetting = QWidget()
        self.tabSetting.setObjectName(u"tabSetting")
        self.verticalLayout_5 = QVBoxLayout(self.tabSetting)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, -1, -1)
        self.label_7 = QLabel(self.tabSetting)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.comboTreeType = QComboBox(self.tabSetting)
        self.comboTreeType.addItem("")
        self.comboTreeType.addItem("")
        self.comboTreeType.addItem("")
        self.comboTreeType.setObjectName(u"comboTreeType")
        self.comboTreeType.setEditable(False)
        self.comboTreeType.setCurrentText(u"ID3")

        self.verticalLayout_4.addWidget(self.comboTreeType)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tabSetting, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.pushButtonBuildTree = QPushButton(self.tab)
        self.pushButtonBuildTree.setObjectName(u"pushButtonBuildTree")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonBuildTree.sizePolicy().hasHeightForWidth())
        self.pushButtonBuildTree.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.pushButtonBuildTree, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.pushButtonRunTest = QPushButton(self.tab)
        self.pushButtonRunTest.setObjectName(u"pushButtonRunTest")

        self.verticalLayout_7.addWidget(self.pushButtonRunTest, 0, Qt.AlignLeft)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab, "")

        self.MainFrame.addWidget(self.tabWidget)

        self.mainSep2 = QFrame(self.tabDecisionTree)
        self.mainSep2.setObjectName(u"mainSep2")
        self.mainSep2.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.mainSep2.setFrameShadow(QFrame.Plain)
        self.mainSep2.setLineWidth(2)
        self.mainSep2.setFrameShape(QFrame.VLine)

        self.MainFrame.addWidget(self.mainSep2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.tabDecisionTree)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.canvas = QWidget()
        self.canvas.setObjectName(u"canvas")
        self.canvas.setGeometry(QRect(0, 0, 185, 578))
        self.horizontalLayout_7 = QHBoxLayout(self.canvas)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.graphicsView = Canvas(self.canvas)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSceneRect(QRectF(0, 0, 1000, 1000))
        self.graphicsView.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.graphicsView.setDragMode(QGraphicsView.NoDrag)

        self.horizontalLayout_7.addWidget(self.graphicsView)

        self.scrollArea.setWidget(self.canvas)

        self.verticalLayout.addWidget(self.scrollArea)


        self.MainFrame.addLayout(self.verticalLayout)

        self.mainSep1 = QFrame(self.tabDecisionTree)
        self.mainSep1.setObjectName(u"mainSep1")
        self.mainSep1.setFrameShape(QFrame.VLine)
        self.mainSep1.setFrameShadow(QFrame.Sunken)

        self.MainFrame.addWidget(self.mainSep1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.tabDecisionTree)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_6 = QFrame(self.tabDecisionTree)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineRunTime = QLineEdit(self.tabDecisionTree)
        self.lineRunTime.setObjectName(u"lineRunTime")
        self.lineRunTime.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineRunTime, 0, 1, 1, 1)

        self.labelRunTime = QLabel(self.tabDecisionTree)
        self.labelRunTime.setObjectName(u"labelRunTime")

        self.gridLayout_2.addWidget(self.labelRunTime, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.line_3 = QFrame(self.tabDecisionTree)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color: rgb(202, 202, 202);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.tabDecisionTree)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.tabDecisionTree)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"color: rgb(202, 202, 202);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tabDecisionTree)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEval = QLineEdit(self.tabDecisionTree)
        self.lineEval.setObjectName(u"lineEval")
        self.lineEval.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEval, 1, 1, 1, 1)

        self.label_2 = QLabel(self.tabDecisionTree)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineOther = QLineEdit(self.tabDecisionTree)
        self.lineOther.setObjectName(u"lineOther")
        self.lineOther.setReadOnly(True)

        self.gridLayout.addWidget(self.lineOther, 2, 1, 1, 1)

        self.lineEvidence = QLineEdit(self.tabDecisionTree)
        self.lineEvidence.setObjectName(u"lineEvidence")
        self.lineEvidence.setEnabled(True)
        self.lineEvidence.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEvidence, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tabDecisionTree)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.line_5 = QFrame(self.tabDecisionTree)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_5)

        self.label_11 = QLabel(self.tabDecisionTree)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.tabDecisionTree)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEditacc = QLineEdit(self.tabDecisionTree)
        self.lineEditacc.setObjectName(u"lineEditacc")
        self.lineEditacc.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEditacc)

        self.label_13 = QLabel(self.tabDecisionTree)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.tabDecisionTree)
        self.tableView.setObjectName(u"tableView")
        self.tableView.horizontalHeader().setMinimumSectionSize(10)
        self.tableView.horizontalHeader().setDefaultSectionSize(40)
        self.tableView.verticalHeader().setMinimumSectionSize(10)
        self.tableView.verticalHeader().setDefaultSectionSize(25)

        self.verticalLayout_2.addWidget(self.tableView)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.MainFrame.addLayout(self.verticalLayout_2)

        self.MainFrame.setStretch(2, 2)

        self.verticalLayout_6.addLayout(self.MainFrame)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.tabWidget_2.addTab(self.tabDecisionTree, "")
        self.tabBN = QWidget()
        self.tabBN.setObjectName(u"tabBN")
        self.horizontalLayout_10 = QHBoxLayout(self.tabBN)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tabWidget_3 = QTabWidget(self.tabBN)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy1.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy1)
        self.tabWidget_3.setMaximumSize(QSize(300, 16777215))
        self.tabBNData = QWidget()
        self.tabBNData.setObjectName(u"tabBNData")
        self.horizontalLayout_9 = QHBoxLayout(self.tabBNData)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_15 = QLabel(self.tabBNData)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_8.addWidget(self.label_15)

        self.pushButtonDir = QPushButton(self.tabBNData)
        self.pushButtonDir.setObjectName(u"pushButtonDir")

        self.verticalLayout_8.addWidget(self.pushButtonDir, 0, Qt.AlignLeft)

        self.label_16 = QLabel(self.tabBNData)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.listView = QListView(self.tabBNData)
        self.listView.setObjectName(u"listView")
        sizePolicy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy1)
        self.listView.setMaximumSize(QSize(220, 16777215))

        self.verticalLayout_8.addWidget(self.listView)

        self.label_14 = QLabel(self.tabBNData)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.tableView_2 = QTableView(self.tabBNData)
        self.tableView_2.setObjectName(u"tableView_2")
        sizePolicy1.setHeightForWidth(self.tableView_2.sizePolicy().hasHeightForWidth())
        self.tableView_2.setSizePolicy(sizePolicy1)
        self.tableView_2.setMaximumSize(QSize(220, 16777215))
        self.tableView_2.horizontalHeader().setMinimumSectionSize(10)
        self.tableView_2.horizontalHeader().setDefaultSectionSize(40)
        self.tableView_2.verticalHeader().setMinimumSectionSize(10)
        self.tableView_2.verticalHeader().setDefaultSectionSize(25)

        self.verticalLayout_8.addWidget(self.tableView_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget_3.addTab(self.tabBNData, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_10.addWidget(self.label_21)

        self.pushButtongenerateBN = QPushButton(self.tab_3)
        self.pushButtongenerateBN.setObjectName(u"pushButtongenerateBN")

        self.verticalLayout_10.addWidget(self.pushButtongenerateBN, 0, Qt.AlignLeft)

        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setTextFormat(Qt.AutoText)

        self.verticalLayout_10.addWidget(self.label_17)

        self.pushButtonQuery = QPushButton(self.tab_3)
        self.pushButtonQuery.setObjectName(u"pushButtonQuery")

        self.verticalLayout_10.addWidget(self.pushButtonQuery, 0, Qt.AlignLeft)

        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_10.addWidget(self.label_18)

        self.labelvar = QLabel(self.tab_3)
        self.labelvar.setObjectName(u"labelvar")

        self.verticalLayout_10.addWidget(self.labelvar)

        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_10.addWidget(self.label_19)

        self.labelcond = QLabel(self.tab_3)
        self.labelcond.setObjectName(u"labelcond")

        self.verticalLayout_10.addWidget(self.labelcond)

        self.pushButtonInfer = QPushButton(self.tab_3)
        self.pushButtonInfer.setObjectName(u"pushButtonInfer")

        self.verticalLayout_10.addWidget(self.pushButtonInfer, 0, Qt.AlignLeft)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_10.addWidget(self.label_20)

        self.lineEditprob = QLineEdit(self.tab_3)
        self.lineEditprob.setObjectName(u"lineEditprob")
        self.lineEditprob.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.lineEditprob)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.tabWidget_3.addTab(self.tab_3, "")

        self.horizontalLayout_11.addWidget(self.tabWidget_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.graphicsView_2 = QGraphicsView(self.tabBN)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_9.addWidget(self.graphicsView_2)


        self.horizontalLayout_11.addLayout(self.verticalLayout_9)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.tabWidget_2.addTab(self.tabBN, "")

        self.horizontalLayout_13.addWidget(self.tabWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.comboTreeType.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u6570\u636e", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6570\u636e", None))
        self.pushButtonTest.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u6570\u636e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u51b3\u7b56\u6811\u7c7b\u578b", None))
        self.comboTreeType.setItemText(0, QCoreApplication.translate("MainWindow", u"ID3", None))
        self.comboTreeType.setItemText(1, QCoreApplication.translate("MainWindow", u"C4.5", None))
        self.comboTreeType.setItemText(2, QCoreApplication.translate("MainWindow", u"CART", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u51b3\u7b56\u6811", None))
        self.pushButtonBuildTree.setText(QCoreApplication.translate("MainWindow", u"Build Tree", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u6d4b\u8bd5", None))
        self.pushButtonRunTest.setText(QCoreApplication.translate("MainWindow", u"Run test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u51b3\u7b56\u6811\u5c5e\u6027", None))
        self.labelRunTime.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8282\u70b9\u5c5e\u6027", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b\u4f9d\u636e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\u6307\u6807", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u7ed3\u679c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u51c6\u786e\u7387", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabDecisionTree), QCoreApplication.translate("MainWindow", u"\u51b3\u7b56\u6811", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u6570\u636e", None))
        self.pushButtonDir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u5185\u5bb9", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u8d1d\u53f6\u65af\u7f51\u7edc\u6570\u636e", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabBNData), QCoreApplication.translate("MainWindow", u"\u6570\u636e", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u8d1d\u53f6\u65af\u7f51\u7edc", None))
        self.pushButtongenerateBN.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.pushButtonQuery.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u67e5\u8be2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.labelvar.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.labelcond.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButtonInfer.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u540e\u9a8c\u6982\u7387", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabBN), QCoreApplication.translate("MainWindow", u"\u8d1d\u53f6\u65af\u7f51\u7edc", None))
    # retranslateUi

