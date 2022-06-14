import pandas as pd 
from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self,data):
        super().__init__()
        self.data_:pd.DataFrame = data 
    
    def data(self,index,role):
        if role == Qt.DisplayRole:
            value = self.data_.iloc[index.row(),index.column()]
            return str(value)
        
    def rowCount(self,index):
        return self.data_.shape[0] 
    
    def columnCount(self,index):
        return self.data_.shape[1] 

    def headerData(self,section,orientation,role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.data_.columns[section])
            
            if orientation == Qt.Vertical:
                return str(self.data_.index[section])
