# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 850)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.MainFrame = QHBoxLayout()
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setSizeConstraint(QLayout.SetMaximumSize)
        self.tabWidget = QTabWidget(self.centralwidget)
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

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab, "")

        self.MainFrame.addWidget(self.tabWidget)

        self.mainSep2 = QFrame(self.centralwidget)
        self.mainSep2.setObjectName(u"mainSep2")
        self.mainSep2.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.mainSep2.setFrameShadow(QFrame.Plain)
        self.mainSep2.setLineWidth(2)
        self.mainSep2.setFrameShape(QFrame.VLine)

        self.MainFrame.addWidget(self.mainSep2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
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
        self.canvas.setGeometry(QRect(0, 0, 697, 765))
        self.scrollArea.setWidget(self.canvas)

        self.verticalLayout.addWidget(self.scrollArea)


        self.MainFrame.addLayout(self.verticalLayout)

        self.mainSep1 = QFrame(self.centralwidget)
        self.mainSep1.setObjectName(u"mainSep1")
        self.mainSep1.setFrameShape(QFrame.VLine)
        self.mainSep1.setFrameShadow(QFrame.Sunken)

        self.MainFrame.addWidget(self.mainSep1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelNodeNum = QLabel(self.centralwidget)
        self.labelNodeNum.setObjectName(u"labelNodeNum")

        self.gridLayout_2.addWidget(self.labelNodeNum, 1, 0, 1, 1)

        self.labelRunTime = QLabel(self.centralwidget)
        self.labelRunTime.setObjectName(u"labelRunTime")

        self.gridLayout_2.addWidget(self.labelRunTime, 0, 0, 1, 1)

        self.lineRunTime = QLineEdit(self.centralwidget)
        self.lineRunTime.setObjectName(u"lineRunTime")

        self.gridLayout_2.addWidget(self.lineRunTime, 0, 1, 1, 1)

        self.lineNodeNum = QLineEdit(self.centralwidget)
        self.lineNodeNum.setObjectName(u"lineNodeNum")

        self.gridLayout_2.addWidget(self.lineNodeNum, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color: rgb(202, 202, 202);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"color: rgb(202, 202, 202);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEval = QLineEdit(self.centralwidget)
        self.lineEval.setObjectName(u"lineEval")

        self.gridLayout.addWidget(self.lineEval, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineOther = QLineEdit(self.centralwidget)
        self.lineOther.setObjectName(u"lineOther")

        self.gridLayout.addWidget(self.lineOther, 2, 1, 1, 1)

        self.lineEvidence = QLineEdit(self.centralwidget)
        self.lineEvidence.setObjectName(u"lineEvidence")
        self.lineEvidence.setEnabled(True)

        self.gridLayout.addWidget(self.lineEvidence, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.MainFrame.addLayout(self.verticalLayout_2)

        self.MainFrame.setStretch(2, 2)

        self.verticalLayout_6.addLayout(self.MainFrame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1276, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboTreeType.setCurrentIndex(0)


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

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u51b3\u7b56\u6811", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Build Tree", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u6d4b\u8bd5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Run test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u51b3\u7b56\u6811\u5c5e\u6027", None))
        self.labelNodeNum.setText(QCoreApplication.translate("MainWindow", u"\u8282\u70b9\u4e2a\u6570", None))
        self.labelRunTime.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8282\u70b9\u5c5e\u6027", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b\u4f9d\u636e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\u6307\u6807", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
    # retranslateUi

