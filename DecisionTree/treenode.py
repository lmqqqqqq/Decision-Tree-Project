class Node:
    def __init__(self,name,value,gain) -> None:
        self.name = name
        self.value = value # 节点分类对应的feature值，root节点的value为None
        self.gain = gain 
        self.isLeaf = False 
        self.children = [] 
    
    def print(self):
        print(f"name:{self.name}")
        if self.value is not None:
            print(f"value:{self.value}")
        print(f"gain:{self.gain}")
        print(f"isleaf:{self.isLeaf}")
        for node in self.children:
            node.print()

    
# 由节点数据结构构成的决策树
class TreeNode:
    def __init__(self) -> None:
        self.root = None
    
    def fromDict(self,dict):
        self.root = TreeNode._fromDict(dict,None)

    def print(self):
        if self.root is not None:
            self.root.print()

    @staticmethod
    def _fromDict(d,feature): 
        # d: dict (non-leaf), str(leaf)
        # @ feature: 存储上一次分类的时候对应分类依据的值
        root = Node(None,None,None)
        if isinstance(d,dict):
            k = list(d.keys())[0] # (name, gain) tuple 
            v = list(d.values())[0] # dict 

            root.name = k[0] 
            root.gain = k[1]
            root.value = feature
            root.isLeaf = False
            for key,value in v.items():
                nextFeature = key 
                root.children.append(TreeNode._fromDict(value,nextFeature))
        
        else :
            root.name = d # 值为分类结果
            root.gain = None 
            root.value = feature
            root.isLeaf = True
            
        return root 

        
if __name__ == "__main__":
    from tree import Decision_Tree
    filename = 'dataset.txt'
    testfile = 'testset.txt'

    T = Decision_Tree()
    dataset, labels = T.read_dataset(filename)

    # ID3决策树
    labels_tmp = labels[:]  # 拷贝，createTree会改变labels
    ID3desicionTree = T.ID3_createTree(
        dataset, labels_tmp, test_dataset=T.read_testset(testfile))
    # print('ID3desicionTree:\n', ID3desicionTree)
    # testSet = T.read_testset(testfile)
    # print("下面为测试数据集结果：")
    # print('ID3_TestSet_classifyResult:\n', T.classifytest(
    #     ID3desicionTree, labels, testSet))
    # print('测试数据集正确率：',
    #         100 * T.cal_acc(T.classifytest(ID3desicionTree, labels, testSet), [ans[-1] for ans in testSet]), '%')
    # print("---------------------------------------------")
    testtree = TreeNode()
    testtree.fromDict(ID3desicionTree)
    testtree.print()
