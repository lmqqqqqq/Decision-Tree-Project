from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QApplication,QGraphicsItem
from PySide6.QtGui import QColor,QPen,QBrush,QFont,QPainter,QPainterPath
from PySide6.QtCore import Qt,QRectF,QPointF
import PySide6
from DecisionTree import Node
from .edgeitem import GraphicEdge

class NodeItem(QGraphicsItem):
    def __init__(self,maxX,node:Node=None,parent=None):
        super().__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable,True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges,True)
        self.setFlag(QGraphicsItem.ItemIsFocusable,True)
        self.state = 0 # 0: not selected, 1: selected
        self.x = 0
        self.y = 0
        self.h_interval =max(min(120,1000/maxX),40)
        self.v_interval =100 
        self.brush = QBrush()
        self.brush.setColor(QColor(220,220,220))
        self.brush.setStyle(Qt.Dense1Pattern)
        self.maxX = maxX

        self.width  = self.h_interval / 1.2
        self.height = 50 
        self.srcedges = [] 
        self.dstedges = []
        if node is not None: 
            self.fromNode(node)
        
    def boundingRect(self) -> PySide6.QtCore.QRectF:
        # return super().boundingRect()
        penWidth = 1
        return QRectF(self.x-penWidth/2,self.y-penWidth/2,self.x+self.width+penWidth/2,self.y+self.height+penWidth/2)

    def fromNode(self,node:Node):
        # messages
        self.x = int(node.x * self.h_interval+100) # 坐标映射
        self.y = int(node.y * self.v_interval+50)
        self.name = node.name
        self.gain = node.gain 
        self.value = node.value 
   
    def paint(self,painter:QPainter,style,*args,**kawrgs):
        painter.setBrush(self.brush)

        pen = QPen()
        pen.setWidth(1)
        painter.setPen(pen)
        # painter.drawRect(self.x,self.y,self.width,self.height)
        painter.drawRoundedRect(self.x,self.y,self.width,self.height,10,10)
        # draw name 
        textHeight = 20
        yinterval = 5
        xinterval = 15
        if self.maxX <= 20 : 
            painter.drawText(self.x,self.y,self.width,textHeight,Qt.AlignHCenter,f"{self.name}")
            if self.gain is not None:
                painter.drawText(self.x+xinterval,self.y+textHeight+yinterval,f"InfoGain: {self.gain}")
        # painter.drawText(self.x,self.y+textHeight*2+yinterval,self.width,textHeight,Qt.AlignLeft,f"{self.name}")

    def print(self):
        print(self.name)
        print(self.x,self.y)
        print(self.gain)
        print("-------------")
    
    # def mousePressEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent) -> None:
    #     if self.isSelected():
    #         self.state = ~self.state 

    #         if self.state == 0:
    #             self.brush.setColor(QColor(220,220,220))
    #         else:
    #             self.brush.setColor(QColor(180,180,180))
    #     super().mousePressEvent(event)

            
