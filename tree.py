from math import log
import operator
from collections import Counter


class Decision_Tree():

    pre_pruning = True
    post_pruning = True
    choice = '1'


    def read_dataset(self, filename):
        """
        年龄段：0代表青年，1代表中年，2代表老年；
        有工作：0代表否，1代表是；
        有自己的房子：0代表否，1代表是；
        信贷情况：0代表一般，1代表好，2代表非常好；
        类别(是否给贷款)：0代表否，1代表是
        """
        fr = open(filename, 'r')
        all_lines = fr.readlines()  # list形式,每行为1个str
        labels = ['年龄段', '有工作', '有自己的房子', '信贷情况']
        dataset = []
        for line in all_lines[0:]:
            line = line.strip().split(',')  # 以逗号为分割符拆分列表
            dataset.append(line)
        return dataset, labels

    def read_testset(self, testfile):
        """
        年龄段：0代表青年，1代表中年，2代表老年；
        有工作：0代表否，1代表是；
        有自己的房子：0代表否，1代表是；
        信贷情况：0代表一般，1代表好，2代表非常好；
        类别(是否给贷款)：0代表否，1代表是
        """
        fr = open(testfile, 'r')
        all_lines = fr.readlines()
        testset = []
        for line in all_lines[0:]:
            line = line.strip().split(',')  # 以逗号为分割符拆分列表
            testset.append(line)
        return testset

    # 计算信息熵
    def cal_entropy(self, dataset):
        numEntries = len(dataset)
        labelCounts = {}
        # 给所有可能分类创建字典
        for featVec in dataset:
            currentlabel = featVec[-1]
            if currentlabel not in labelCounts.keys():
                labelCounts[currentlabel] = 0
            labelCounts[currentlabel] += 1
        Ent = 0.0
        for key in labelCounts:
            p = float(labelCounts[key]) / numEntries
            Ent = Ent - p * log(p, 2)  # 以2为底求对数
        return Ent

    # 划分数据集
    def splitdataset(self, dataset, axis, value):
        retdataset = []  # 创建返回的数据集列表
        for featVec in dataset:  # 抽取符合划分特征的值
            if featVec[axis] == value:
                reducedfeatVec = featVec[:axis]  # 去掉axis特征
                reducedfeatVec.extend(featVec[axis + 1:])  # 将符合条件的特征添加到返回的数据集列表
                retdataset.append(reducedfeatVec)
        return retdataset

    # 利用ID3算法选择最优划分属性
    def ID3_chooseBestFeatureToSplit(self, dataset):
        numFeatures = len(dataset[0]) - 1
        baseEnt = self.cal_entropy(dataset)
        bestInfoGain = 0.0
        bestFeature = -1
        for i in range(numFeatures):  # 遍历所有特征
            featList = [example[i] for example in dataset]
            uniqueVals = set(featList)  # 将特征列表创建成为set集合，元素不可重复。创建唯一的分类标签列表
            newEnt = 0.0
            for value in uniqueVals:  # 计算每种划分方式的信息熵
                subdataset = self.splitdataset(dataset, i, value)
                p = len(subdataset) / float(len(dataset))
                newEnt += p * self.cal_entropy(subdataset)
            infoGain = baseEnt - newEnt
            print(u"ID3中第%d个特征的信息增益为：%.3f" % (i, infoGain))
            if (infoGain > bestInfoGain):
                bestInfoGain = infoGain  # 计算最好的信息增益
                bestFeature = i
        return bestFeature

    # 利用C4.5算法选择最优划分属性
    def C45_chooseBestFeatureToSplit(self, dataset):
        numFeatures = len(dataset[0]) - 1
        baseEnt = self.cal_entropy(dataset)
        bestInfoGain_ratio = 0.0
        bestFeature = -1
        for i in range(numFeatures):  # 遍历所有特征
            featList = [example[i] for example in dataset]
            uniqueVals = set(featList)  # 将特征列表创建成为set集合，元素不可重复。创建唯一的分类标签列表
            newEnt = 0.0
            IV = 0.0
            for value in uniqueVals:  # 计算每种划分方式的信息熵
                subdataset = self.splitdataset(dataset, i, value)
                p = len(subdataset) / float(len(dataset))
                newEnt += p * self.cal_entropy(subdataset)
                IV = IV - p * log(p, 2)
            infoGain = baseEnt - newEnt
            if (IV == 0):
                continue
            infoGain_ratio = infoGain / IV  # 这个feature的infoGain_ratio
            print(u"C4.5中第%d个特征的信息增益率为：%.3f" % (i, infoGain_ratio))
            if (infoGain_ratio > bestInfoGain_ratio):  # 选择最大的gain ratio
                bestInfoGain_ratio = infoGain_ratio
                bestFeature = i  # 选择最大的gain ratio对应的feature
        return bestFeature

    # 以样本中的多数确定叶子结点的分类
    def majorityCnt(self, classList):
        '''
        数据集已经处理了所有属性，但是类标签依然不是唯一的，以样本中的多数确定叶子结点的分类
        '''
        classCont = {}
        for vote in classList:
            if vote not in classCont.keys():
                classCont[vote] = 0
            classCont[vote] += 1
        sortedClassCont = sorted(classCont.items(), key=operator.itemgetter(1), reverse=True)  # 降序排序
        return sortedClassCont[0][0]

    # 利用ID3算法创建决策树
    def ID3_createTree(self, dataset, labels, test_dataset):
        classList = [example[-1] for example in dataset]
        if classList.count(classList[0]) == len(classList):
            # 类别完全相同，停止划分
            return classList[0]
        if len(dataset[0]) == 1:
            # 遍历完所有特征时返回出现次数最多的
            return self.majorityCnt(classList)
        bestFeat = self.ID3_chooseBestFeatureToSplit(dataset)
        bestFeatLabel = labels[bestFeat]
        print(u"此时最优索引为：" + (bestFeatLabel))

        ID3Tree = {bestFeatLabel: {}}
        del (labels[bestFeat])
        # 得到列表包括节点所有的属性值
        featValues = [example[bestFeat] for example in dataset]
        uniqueVals = set(featValues)

        # 进行预剪枝
        if self.pre_pruning:
            ans = []
            for index in range(len(test_dataset)):
                ans.append(test_dataset[index][-1])
            result_counter = Counter()
            for vec in dataset:
                result_counter[vec[-1]] += 1
            leaf_output = result_counter.most_common(1)[0][0]  # 此时该结点为叶子结点
            root_acc = self.cal_acc(test_output=[leaf_output] * len(test_dataset), label=ans)  # 不对该结点再进行划分时的正确率
            outputs = []
            ans = []
            for value in uniqueVals:  # 对该结点进行划分
                cut_testset = self.splitdataset(test_dataset, bestFeat, value)
                cut_dataset = self.splitdataset(dataset, bestFeat, value)
                for vec in cut_testset:
                    ans.append(vec[-1])
                result_counter = Counter()
                for vec in cut_dataset:
                    result_counter[vec[-1]] += 1
                leaf_output = result_counter.most_common(1)[0][0]
                outputs += [leaf_output] * len(cut_testset)
            cut_acc = self.cal_acc(test_output=outputs, label=ans)  # 对该结点再进行划分时的正确率

            if cut_acc <= root_acc:
                return leaf_output

        for value in uniqueVals:  # 此时不进行预剪枝，对该结点进行划分
            subLabels = labels[:]
            ID3Tree[bestFeatLabel][value] = self.ID3_createTree(
                self.splitdataset(dataset, bestFeat, value),
                subLabels,
                self.splitdataset(test_dataset, bestFeat, value))

        # 进行后剪枝
        if self.post_pruning:
            tree_output = self.classifytest(ID3Tree,
                                            featLabels=['年龄段', '有工作', '有自己的房子', '信贷情况'],
                                            testDataSet=test_dataset)
            ans = []
            for vec in test_dataset:
                ans.append(vec[-1])
            root_acc = self.cal_acc(tree_output, ans)  # 不进行后剪枝的正确率
            result_counter = Counter()
            for vec in dataset:
                result_counter[vec[-1]] += 1
            leaf_output = result_counter.most_common(1)[0][0]
            cut_acc = self.cal_acc([leaf_output] * len(test_dataset), ans)  # 不需要划分，将分支剪除（相当于替换为叶结点）的正确率

            if cut_acc >= root_acc:
                return leaf_output

        return ID3Tree

    # 利用C4.5算法创建决策树
    def C45_createTree(self, dataset, labels, test_dataset):
        classList = [example[-1] for example in dataset]
        if classList.count(classList[0]) == len(classList):
            # 类别完全相同，停止划分
            return classList[0]
        if len(dataset[0]) == 1:
            # 遍历完所有特征时返回出现次数最多的
            return self.majorityCnt(classList)
        bestFeat = self.C45_chooseBestFeatureToSplit(dataset)
        bestFeatLabel = labels[bestFeat]
        print(u"此时最优索引为：" + (bestFeatLabel))
        C45Tree = {bestFeatLabel: {}}
        del (labels[bestFeat])
        # 得到列表包括节点所有的属性值
        featValues = [example[bestFeat] for example in dataset]
        uniqueVals = set(featValues)

        # 进行预剪枝
        if self.pre_pruning:
            ans = []
            for index in range(len(test_dataset)):
                ans.append(test_dataset[index][-1])
            result_counter = Counter()
            for vec in dataset:
                result_counter[vec[-1]] += 1
            leaf_output = result_counter.most_common(1)[0][0]  # 此时该结点为叶子结点
            root_acc = self.cal_acc(test_output=[leaf_output] * len(test_dataset), label=ans)  # 不对该结点再进行划分时的正确率
            outputs = []
            ans = []
            for value in uniqueVals:  # 对该结点进行划分
                cut_testset = self.splitdataset(test_dataset, bestFeat, value)
                cut_dataset = self.splitdataset(dataset, bestFeat, value)
                for vec in cut_testset:
                    ans.append(vec[-1])
                result_counter = Counter()
                for vec in cut_dataset:
                    result_counter[vec[-1]] += 1
                leaf_output = result_counter.most_common(1)[0][0]
                outputs += [leaf_output] * len(cut_testset)
            cut_acc = self.cal_acc(test_output=outputs, label=ans)  # 对该结点再进行划分时的正确率

            if cut_acc <= root_acc:
                return leaf_output

        for value in uniqueVals:  # 此时不进行预剪枝，对该结点进行划分
            subLabels = labels[:]
            C45Tree[bestFeatLabel][value] = self.C45_createTree(
                self.splitdataset(dataset, bestFeat, value),
                subLabels,
                self.splitdataset(test_dataset, bestFeat, value))

        # 进行后剪枝
        if self.post_pruning:
            tree_output = self.classifytest(C45Tree,
                                            featLabels=['年龄段', '有工作', '有自己的房子', '信贷情况'],
                                            testDataSet=test_dataset)
            ans = []
            for vec in test_dataset:
                ans.append(vec[-1])
            root_acc = self.cal_acc(tree_output, ans)  # 不进行后剪枝的正确率
            result_counter = Counter()
            for vec in dataset:
                result_counter[vec[-1]] += 1
            leaf_output = result_counter.most_common(1)[0][0]
            cut_acc = self.cal_acc([leaf_output] * len(test_dataset), ans)  # 不需要划分，将分支剪除（相当于替换为叶结点）的正确率

            if cut_acc >= root_acc:
                return leaf_output

        return C45Tree

    def classify(self, inputTree, featLabels, testVec):
        """
        输入：决策树，分类标签，测试数据
        输出：决策结果
        描述：利用决策树对测试数据进行测试，输出每个测试数据的结果
        """
        firstStr = list(inputTree.keys())[0]
        secondDict = inputTree[firstStr]
        featIndex = featLabels.index(firstStr)
        classLabel = '0'
        for key in secondDict.keys():
            if testVec[featIndex] == key:
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = self.classify(secondDict[key], featLabels, testVec)
                else:
                    classLabel = secondDict[key]
        return classLabel

    def classifytest(self, inputTree, featLabels, testDataSet):
        """
        输入：决策树，分类标签，测试数据
        输出：决策结果
        描述：利用决策树对测试数据进行测试，输出所有测试数据的结果
        """
        classLabelAll = []
        for testVec in testDataSet:
            classLabelAll.append(self.classify(inputTree, featLabels, testVec))
        return classLabelAll

    # 计算测试集的正确率
    def cal_acc(self, test_output, label):
        count = 0
        for index in range(len(test_output)):
            if test_output[index] == label[index]:
                count += 1

        return float(count / len(test_output))


if __name__ == '__main__':
    filename = 'dataset.txt'
    testfile = 'testset.txt'

    T = Decision_Tree()
    dataset, labels = T.read_dataset(filename)

    T.choice = input('请输入建树方式：1（ID3），2（C4.5）')

    print('下面开始创建相应的决策树-------')


    # ID3决策树
    if T.choice == '1':
        labels_tmp = labels[:]  # 拷贝，createTree会改变labels
        ID3desicionTree = T.ID3_createTree(dataset, labels_tmp, test_dataset=T.read_testset(testfile))
        print('ID3desicionTree:\n', ID3desicionTree)
        testSet = T.read_testset(testfile)
        print("下面为测试数据集结果：")
        print('ID3_TestSet_classifyResult:\n', T.classifytest(ID3desicionTree, labels, testSet))
        print("---------------------------------------------")

    # C4.5决策树
    if T.choice == '2':
        labels_tmp = labels[:]  # 拷贝，createTree会改变labels
        C45desicionTree = T.C45_createTree(dataset, labels_tmp, test_dataset=T.read_testset(testfile))
        print('C45desicionTree:\n', C45desicionTree)
        testSet = T.read_testset(testfile)
        print("下面为测试数据集结果：")
        print('C4.5_TestSet_classifyResult:\n', T.classifytest(C45desicionTree, labels, testSet))
        print("---------------------------------------------")
