class Node:
    def __init__(self,name,value,gain,parent) -> None:
        self.name = name
        self.value = value # 节点分类对应的feature值，root节点的value为None
        self.gain = gain 
        self.isLeaf = False 
        self.x = -1
        self.y = 0
        self.offset = 0
        self.ancestor = self
        self.children = [] 
        self.change = self.shift = 0
        self._lmost_sibling = None # the number of the node in its group of siblings
        self.number = None

        self.parent:Node = parent
    
    def left_brother(self):
        n = None 
        if self.parent : 
            for node in self.parent.children:
                if node == self: 
                    return n
                else: 
                    n = node 
        return n 
    
    def get_lmost_sibling(self):
        if not self._lmost_sibling and self.parent and self != \
            self.parent.children[0]:
            self._lmost_sibling = self.parent.children[0] 
        return self._lmost_sibling
    
    leftmost_sibling = property(get_lmost_sibling)
    
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
        self.root = TreeNode._fromDict(dict,None,None,0,1)
    
    def calculatePosition(self):
        self.root = TreeNode.buchheim(self.root)

    def print(self):
        if self.root is not None:
            self.root.print()

    @staticmethod
    def _fromDict(d,feature,parent,depth=0,number=1): 
        # d: dict (non-leaf), str(leaf)
        # @ feature: 存储上一次分类的时候对应分类依据的值
        root = Node(None,None,None,parent)
        if isinstance(d,dict):
            k = list(d.keys())[0] # (name, gain) tuple 
            v = list(d.values())[0] # dict 

            root.name = k[0] 
            root.gain = k[1]
            root.value = feature
            root.isLeaf = False
            root.parent = parent
            root.y = depth
            root.number = number
            for index,dicts in enumerate(list(enumerate(v))):
                key,value = dicts  # '0': {} ; '1':{}
                nextFeature = key 
                root.children.append(TreeNode._fromDict(value,nextFeature,root,depth+1,index+1))
        
        else :
            root.name = d # 值为分类结果
            root.gain = None 
            root.value = feature
            root.isLeaf = True
            root.parent = parent
            root.number = number
            root.y = depth
            
        return root 
    @staticmethod
    def buchheim(tree):
        dt = TreeNode.firstwalk(tree)
        TreeNode.second_walk(dt)
        return dt

    @staticmethod
    def firstwalk(v, distance=1.):
        if len(v.children) == 0:
            if v.leftmost_sibling:
                v.x = v.left_brother().x + distance
            else:
                v.x = 0.
        else:
            default_ancestor = v.children[0]
            for w in v.children:
                TreeNode.firstwalk(w)
                default_ancestor = TreeNode.apportion(w, default_ancestor,
                                            distance)
            TreeNode.execute_shifts(v)

            midpoint = (v.children[0].x + v.children[-1].x) / 2

            ell = v.children[0]
            arr = v.children[-1]
            w = v.left_brother()
            if w:
                v.x = w.x + distance
                v.mod = v.x - midpoint
            else:
                v.x = midpoint
        return v
    @staticmethod
    def apportion(v, default_ancestor, distance):
        w = v.left_brother()
        if w is not None:
            #in buchheim notation:
            #i == inner; o == outer; r == right; l == left;
            vir = vor = v
            vil = w
            vol = v.leftmost_sibling
            sir = sor = v.mod
            sil = vil.mod
            sol = vol.mod
            while vil.right() and vir.left():
                vil = vil.right()
                vir = vir.left()
                vol = vol.left()
                vor = vor.right()
                vor.ancestor = v
                shift = (vil.x + sil) - (vir.x + sir) + distance
                if shift > 0:
                    a = TreeNode.ancestor(vil, v, default_ancestor)
                    TreeNode.move_subtree(a, v, shift)
                    sir = sir + shift
                    sor = sor + shift
                sil += vil.mod
                sir += vir.mod
                sol += vol.mod
                sor += vor.mod
            if vil.right() and not vor.right():
                vor.thread = vil.right()
                vor.mod += sil - sor
            else:
                if vir.left() and not vol.left():
                    vol.thread = vir.left()
                    vol.mod += sir - sol
                default_ancestor = v
        return default_ancestor
    @staticmethod
    def move_subtree(wl, wr, shift):
        subtrees = wr.number - wl.number
        wr.change -= shift / subtrees
        wr.shift += shift
        wl.change += shift / subtrees
        wr.x += shift
        wr.mod += shift
    @staticmethod
    def execute_shifts(v):
        shift = change = 0
        for w in v.children[::-1]:
            w.x += shift
            w.mod += shift
            change += w.change
            shift += w.shift + change

    def ancestor(vil, v, default_ancestor):
        if vil.ancestor in v.parent.children:
            return vil.ancestor
        else:
            return default_ancestor
    @staticmethod
    def second_walk(v, m=0, depth=0):
        v.x += m
        v.y = depth

        for w in v.children:
            TreeNode.second_walk(w, m + v.mod, depth+1, min)

        
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
