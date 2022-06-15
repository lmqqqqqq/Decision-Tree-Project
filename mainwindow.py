from time import time

from DecisionTree.tree import Decision_Tree
from mainwindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication,QFileDialog
from PySide6.QtCore import Slot,QStringListModel
import pandas as pd
import numpy as np
import time
from BN import *

from module import TableModel,TreeNode,Node,Canvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.treeType = "ID3" # 0: ID3, 1: C4.5 
        self.treeModel = Decision_Tree()
        self.trainFile = None 
        self.testFile = None
        self.testModel = None
        self.trainModel = None 
        self.tree = None # 用于plot tree
        self.connect() 

    def connect(self):
        # define connect signal with slots
        self.ui.openFileButton.clicked.connect(self.openTrainFileDialog)
        self.ui.pushButtonTest.clicked.connect(self.openTestFileDialog)
        self.ui.pushButtonBuildTree.clicked.connect(self.buildTree)
        self.ui.pushButtonRunTest.clicked.connect(self.runTest)
        self.ui.pushButtonDir.clicked.connect(self.openDir)
        self.ui.listView.clicked.connect(self.clicklist)
        self.ui.pushButtongenerateBN.clicked.connect(self.generateBN)
        self.ui.pushButtonInfer.clicked.connect(self.infer)
        self.ui.pushButtonQuery.clicked.connect(self.openQuery)

    """slots"""
    @Slot()
    def openQuery(self):
        filename = QFileDialog.getOpenFileName(self,"Open File","./Query")
        if filename[0]:
            filename = filename[0] 
            self.queryFile = filename
            self.query = Query()
            self.query.fromFile(filename)
            self.ui.labelcond.setText(f"{str(self.query.conditions)}")
            self.ui.labelvar.setText(f"{str(self.query.vars)}")


    @Slot()
    def infer(self):
        prob = self.bayesNet.ask(self.query)
        self.ui.lineEditprob.setText(str(prob))

    @Slot()
    def generateBN(self):
        if self.ui.graphicsViewBN.scene is not None:
            self.ui.graphicsViewBN.scene.clear()
        self.ui.graphicsViewBN.plotBN(self.bayesNet)

    @Slot()
    def openDir(self):
        import os
        dir = "./netstruct"
        folderName = QFileDialog.getExistingDirectory(self,"Open Folder",dir)
        print(folderName)
        if folderName:
            self.folder = folderName
            self.bayesNet = BN()
            self.bayesNet.fromFolder(self.folder)
            self.files = os.listdir(self.folder)
            # 设置文件夹内容
            listModel = QStringListModel()
            listModel.setStringList(self.files)
            self.ui.listView.setModel(listModel)

    @Slot()
    def clicklist(self,item):
        index = item.row()
        filename = self.files[index]
        fullpath = f"{self.folder}/{filename}"
        df = pd.read_csv(fullpath)
        model = TableModel(df)
        self.ui.tableView_2.setModel(model)


    @Slot()
    def openTrainFileDialog(self):
        home_dir = "./DecisionTree"
        fname = QFileDialog.getOpenFileName(self,'Open File',home_dir)
        if fname[0]: 
            self.trainFile = fname[0] 
            df = pd.read_csv(self.trainFile)
            for column in list(df.columns):
                if df[column].dtype ==object :
                    fact,index = pd.factorize(df[column])
                    df[column] = fact 
                if df[column].dtype == np.float64:
                    mean = df[column].mean()
                    bool_index = df[column] > mean
                    df[column][bool_index] = 1
                    df[column][~bool_index] = 0

            if self.trainFile[-9:] == "train.csv":
                df = df.iloc[:,1:]
                order = list(df.columns)
                order = [*order[1:],order[0]]
                df = df[order]
            
            df = df.astype(np.int32)

            self.trainModel = TableModel(df)
            self.ui.tableViewTrain.setModel(self.trainModel)
            testDf = pd.DataFrame([],columns=df.columns)
            self.testModel = TableModel(testDf)
            self.ui.tableViewTest.setModel(self.testModel)
    
    @Slot()
    def openTestFileDialog(self):
        home_dir = "./DecisionTree"
        fname = QFileDialog.getOpenFileName(self,"Open File",home_dir)
        if fname[0]:
            file = fname[0]
            self.testFile = file
            df = pd.read_csv(file)
            for column in list(df.columns):
                if df[column].dtype ==object :
                    fact,index = pd.factorize(df[column])
                    df[column] = fact 
                if df[column].dtype == np.float64:
                    mean = df[column].mean()
                    bool_index = df[column] > mean
                    df[column][bool_index] = 1
                    df[column][~bool_index] = 0

            if self.testFile[-8:] == "test.csv":
                df = df.iloc[:,1:]
                order = list(df.columns)
                df = df[order]
            df = df.astype(np.int32)
            self.testModel = TableModel(df)
            self.ui.tableViewTest.setModel(self.testModel)
    
    @Slot()
    def buildTree(self):
        start_time =time.time()

        self.treeType = self.ui.comboTreeType.currentText()
        self.trainDataset,self.labels = self.treeModel.read_dataset(self.trainFile)
        self.testDataset = self.treeModel.read_testset(self.testFile)
        if self.treeType == "ID3":
            # decisionTree: dict 类型 返回结果
            self.decisionTree = self.treeModel.ID3_createTree(self.trainDataset,self.labels.copy(),test_dataset=self.testDataset)
        elif self.treeType == "C4.5":
            self.decisionTree = self.treeModel.C45_createTree(self.trainDataset,self.labels.copy(),test_dataset=self.testDataset)
        elif self.treeType == "CART":
            self.decisionTree = self.treeModel.CART_createTree(self.trainDataset,self.labels.copy(),test_dataset=self.testDataset)
        
        self.tree = TreeNode(self.decisionTree)
        end_time = time.time()
        self.ui.lineRunTime.setText(f"{end_time-start_time:.2f}")
        #TODO: test
        # self.tree.print()
        
        # plotting 
        if self.ui.graphicsView.scene is not None:
            self.ui.graphicsView.scene.clear()
        self.ui.graphicsView.plotTree(self.tree.maxX,self.tree)

    @Slot()
    def runTest(self):
        self.predict = self.treeModel.classifytest(self.decisionTree,self.labels,self.testDataset)
        self.acc = self.treeModel.cal_acc(self.predict,[ans[-1] for ans in self.testDataset])
        self.ui.lineEditacc.setText(f"{self.acc*100:.2f}")
        df = pd.DataFrame(np.array(self.predict).reshape((-1,1)),columns=[self.labels[-1]])
        self.predcitTable = TableModel(df)
        self.ui.tableView.setModel(self.predcitTable)
        


if __name__ == "__main__":
    import sys 
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show() 
    sys.exit(app.exec())