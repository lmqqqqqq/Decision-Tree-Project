from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QApplication,QGraphicsRectItem
from PySide6.QtGui import QColor,QPen,QBrush,QFont
from PySide6.QtCore import Qt,QRectF
import PySide6
from typing import Union
from DecisionTree import TreeNode,Node
from .nodeitem import GraphicEdge, NodeItem

class GraphScene(QGraphicsScene):
    def __init__(self,parent=None):
        super().__init__(parent)
    
    def drawBackground(self, painter: PySide6.QtGui.QPainter, rect: Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]) -> None:
        return super().drawBackground(painter, rect)

class Canvas(QGraphicsView):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent 
        self.scene:QGraphicsScene = QGraphicsScene()
        self.scene.setSceneRect(0,0,1000,1000)
        self.setScene(self.scene)
    
    def _recursivePlot(self,maxX,node:Node,edge:GraphicEdge):
        nodeitem = NodeItem(maxX,node)
        if edge is not None:
            edge.set_dst(nodeitem)
            # nodeitem.dstedges.append(edge)
            self.scene.addItem(edge)

        # TODO: plot test
        # nodeitem.print()
        self.scene.addItem(nodeitem)
        for child in node.children:
            if not node.isLeaf:
                newedge =GraphicEdge()
                newedge.set_src(nodeitem)
                # nodeitem.srcedges.append(newedge)
            self._recursivePlot(maxX,child,newedge)
        
    def plotTree(self,maxX,tree:TreeNode):
        self._recursivePlot(maxX,tree.root,None)
        self.setScene(self.scene)

