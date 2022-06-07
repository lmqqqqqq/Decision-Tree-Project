"""Bayesian Netowrk Definition""" 
import os
import pandas as pd
from factor import Factor
from node import Node
import numpy as np

class Query():
    def __init__(self):
        """P(vars|conditions)的形式"""
        self.conditions:dict = None  # key 为var的名称，值为 0 或者1表示真或者伪
        self.vars:dict = None 
    
    def fromFile(self,path="testfiles/input.txt"):
        with open(path,"r") as f: 
            lines = f.readlines()
            cols = lines[0].split("\n")[0].split(" ")[0].split(",")
            data = [int(i) for i in lines[1].split(",")]
            self.vars = dict(zip(cols,data))

            cols = lines[2].split("\n")[0].split(" ")[0].split(",")
            data = [int(i) for i in lines[3].split(",")]
            self.conditions = dict(zip(cols,data))
    
    def print(self):
        print(self.conditions)
        print(self.vars)

class BN():

    def __init__(self):
        self.names = list() # list of all names in BN 
        self.nodes = list() # list of all nodes in BN 
        self.nameDict = dict() # dict : node name ->  node index in nodes

    def fromFolder(self,path): 
        """
        一个BN由一个folder + 若干文件构成,每个文件都是一个csv,描述一个node
        """
        files = os.listdir(path)
        for file in files: 
            # 构建 nodes 信息
            node = Node()
            node.fromFile(f"{path}/{file}")
            self.nodes.append(node)
            self.nameDict[node.name] = len(self.nodes)-1 
            self.names.append(node.name)
        
        # self.print()
        
        # 构建 father 和 children 信息
        for index,node in enumerate(self.nodes):
            conditions = node.data.columns.tolist() 
            for condition in conditions[:-1]:
                # print(self.nameDict[condition])
                node.father.append(self.nameDict[condition]) # father 存储索引
                self.nodes[self.nameDict[condition]].children.append(index) # children 存储索引

    def print(self):
        for node in self.nodes:
            print(node.name)
            print("data:\n",node.data)
            print("father:")
            # print(len(node.father))
            for f in node.father: 
                print(self.nodes[f].name,":",id(self.nodes[f]),end=" ")
            print("")

    def sortVars(self):
        # 为结点排拓扑序
        import numpy as np
        from collections import deque
        cntChildren = np.zeros((len(self.names)))
        q = deque()
        for index,name in enumerate(self.names):
            cntChildren[index] = len(self.nodes[self.nameDict[name]].children)
            if cntChildren[index] == 0:
                q.append(index)
        
        result = list()  # 节点拓扑序的index
        while len(q) >0 : 
            front = q.pop()
            result.append(front)
            for f in self.nodes[front].father: 
                cntChildren[f] -= 1
                if cntChildren[f] == 0:
                    q.append(f)
        
        return result
    
    # 查询一个query 在 Bayes 网络中的概率
    def ask(self,query:Query):
        orderedVar =  self.sortVars()
        qvars = list(query.vars.keys())
        qcond = list(query.conditions.keys())

        factor = None
        for index in orderedVar:
            newFactor = Factor() 
            newFactor.fromNode(self.nodes[index],query.conditions)

            if factor is None: 
                factor = newFactor 
            else: 
                factor = factor.mult(newFactor)
                # print("Mult:",end="")
                # factor.print()

            if self.names[index] not in qcond and self.names[index] not in qvars: 
                # 如果是隐藏变量, 则消元
                factor = SumOut(self.names[index],factor)
            # print("Sum:",end="")
            # factor.print()
        # 归一化最后的 factor 结果
        # 假设 查询的var只有一个 
        # TODO: 扩展到更高维
        result_df = factor.data
        arr = factor.data.to_numpy()[:,-1]  # 取出 prob 
        if arr.shape[0] != 2:
            print("Wrong dimension!")
            return 
        alpha = arr.sum()
        arr = arr/alpha 
        var = result_df.columns.to_list()[0]
        pos = result_df[(result_df[var] == query.vars[var])].index.tolist()[0]
        return arr[pos]

def SumOut(name,factor:Factor):
    df = factor.data 
    group = df.groupby(name)

    g1 = group.get_group(0)
    g1 = g1.rename(columns={"Value":"V1"})
    g1 = g1.drop(labels=name,axis=1)
    # print(g1)

    g2 = group.get_group(1)
    g2 = g2.rename(columns={"Value":"V2"})
    g2 = g2.drop(labels=name,axis=1)
    # print(g2)
    
    g = g1.merge(g2) 
    g["V1"] = g["V1"] + g["V2"]
    g = g.drop(labels="V2",axis=1)
    g = g.rename(columns={"V1":"Value"})
    # print(g)

    result = Factor(g) 
    return result

if __name__ == "__main__":
    path = "./BN"
    q = Query() 
    q.fromFile()
    bn = BN()
    bn.fromFolder("../netstruct/")
    prob = bn.ask(q)
    print(prob)
