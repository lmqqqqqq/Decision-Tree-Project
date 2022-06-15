import pandas as pd 

class bayesNode(): 
    """Bayesian Network中的节点"""
    # variables 
    # conditions = list() # string的list，记录所有“条件”
    # prob = dict() # 储存条件概率表. key 为 0,1组成的元组

    def __init__(self):
        self.name = None # 当前节点的名称
        self.data :pd.DataFrame = None
        self.father = list()  # 父节点
        self.children = list() # 孩子结点
        self.x = 0
        self.y = 0

    def fromFile(self,path):
        df = pd.read_csv(path)
        self.data = df 
        self.name = df.columns.tolist()[-1]