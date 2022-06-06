import numpy as np 
import pandas as pd
from node import Node

class Factor():
    def __init__(self,df:pd.DataFrame = None) -> None:
        if df is not None:
            self.data = df.copy() 
            self.vars = df.columns.tolist()[:-1]
        else: 
            self.data = None 
            self.vars = None

    def mult(self,f):
        newVars = list(set(self.vars + f.vars))
        width = 2 ** (len(newVars))
        newData = np.zeros((width,len(newVars)+1))
        mult1 = np.zeros(width)
        mult2 = np.zeros(width)
        
        # 产生所有 (1,1,1) 的组合
        choice = []
        for i in range(width-1,-1,-1):
            subchoice = np.ones((len(newVars)))
            for j in range(len(newVars)):
                subchoice[len(newVars)-1-j] = (i >> j) % 2
            choice.append(subchoice)

        # 处理 mult1
        for index,value in enumerate(choice):
            # value: newvars 的取值组合
            newData[index,:-1] = np.array(value)
            bool_index = True 
            for i,var in enumerate(newVars):
                if var in self.vars :
                    bool_index &= (self.data[var]==value[i]) # 选择df中 var = value[i] 的行(value = 0 /1 )
            mult1[index] = self.data[bool_index].iloc[0,-1]

        # 处理 mult2
        for index,value in enumerate(choice):
            # value: newvars 的取值组合
            bool_index=True
            for i,var in enumerate(newVars):
                if var in f.vars:
                    bool_index &= (f.data[var]==value[i]) #
            mult2[index] = f.data[bool_index].iloc[0,-1]
        
        for index in range(len(choice)):
            newData[index,-1] = mult1[index] * mult2[index]

        newVars.append("Value")
        newDf= pd.DataFrame(newData,columns=newVars)
        names_ = newDf.columns.tolist()[:-1]
        newDf[names_] = newDf[names_].astype(np.int)
        return Factor(newDf)
    
    def fromFile(self,path):
        df = pd.read_csv(path)
        self.data = df.copy()
        self.vars = df.columns.tolist()[:-1]
        lastname = df.columns.tolist()[-1]
        # self.data = self.data.rename(columns = {lastname:"Value"})
   

    def fromNode(self,node:Node,conditions:dict):
        # self.data = node.data
        vars = node.data.columns.tolist()
        # self.data = self.data.rename(columns={lastname:"Value"})
        df = node.data.to_numpy()
        prob = df[:,-1]
        df = df[:,:-1]
        width =2**(len(vars))
        mid = int(width/2)
        newDf = np.zeros((width,len(vars) + 1))
        # lastname = 0 
        newDf[:mid,:-2] = df 
        newDf[:mid,-2] = 0
        newDf[:mid,-1] = prob

        # lastname = 1
        newDf[mid:,:-2] = df
        newDf[mid:,-2] =  1
        newDf[mid:,-1] = 1-prob

        column = vars.copy() 
        column.append("Value")
        newDf = pd.DataFrame(newDf,columns=column)
        newDf[column[:-1]] = newDf[column[:-1]].astype(int)

        # 处理 conditions
        if conditions is not None:
            bool_index = True 
            available_condition = []
            for key,value in conditions.items(): 
                if key in vars:
                    bool_index &= (newDf[key] == value)
                    vars.remove(key) # 删除键
                    available_condition.append(key)
            
            if len(available_condition):
                selectedDf = newDf[bool_index].drop(columns=available_condition)
            else : 
                selectedDf = newDf
            self.vars = vars
            self.data = selectedDf
        else: 
            self.data = newDf
            self.vars = vars
    
    def print(self):
        print(self.vars)
        print(self.data)

if __name__ == "__main__":

    n = Node()
    n.fromFile("./BN/a.csv")
    f1 = Factor()
    f1.fromNode(n,None)
    f1.print()
    f2 = Factor()
    f2.fromFile("./f2.csv")
    f2.print()
    f3 = f1.mult(f2)
    f3.print()

                


