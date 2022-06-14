from PySide6.QtWidgets import QGraphicsView,QGraphicsScene,QApplication,QGraphicsItem
from PySide6.QtGui import QColor,QPen,QBrush,QFont,QPainter,QPainterPath
from PySide6.QtCore import Qt,QRectF,QPointF
import PySide6
from DecisionTree import Node
from typing import Optional

class GraphicEdge(QGraphicsItem):
    def __init__(self, parent: Optional[PySide6.QtWidgets.QGraphicsItem] = None) -> None:
        super().__init__(parent)
        self.width = 1.0
        self.startNode = None
        self.endNode =None
        self.pos_src=  [0,0]
        self.pos_dst = [0,0]
        self.text =None

        self._pen = QPen(QColor("#000"))
        self._pen.setWidthF(self.width)

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setZValue(-1)
    
    def set_src(self,node):
        self.startNode = node
        self.pos_src = [node.x+node.width/2,node.y+node.height] # 在下方正中间
    
    def set_dst(self,node):
        self.endNode = Node
        self.text = str(node.value)
        self.pos_dst = [node.x+node.width/2,node.y] # 在上方正中间
    
    def calc_path(self):
        path = QPainterPath(QPointF(self.pos_src[0], self.pos_src[1]))  # 起点
        path.lineTo(self.pos_dst[0], self.pos_dst[1])  # 终点
        return path
    
    def boundingRect(self):
        return self.shape().boundingRect()
	
	# override
    def shape(self):
        return self.calc_path()
    
    def updatePath(self):
        self.path = self.calc_path()
	
	# override
    def paint(self, painter:QPainter, graphics_item, widget=None):
        if self.startNode is not None and self.endNode is not None:
            # 如果前后两端都添加，则绘制
            self.updatePath()
            painter.setPen(self._pen)
            painter.drawPath(self.path)
            text_width = 100
            text_height= 20
            midpoint = [(self.pos_src[0] + self.pos_dst[0] )/2 ,(self.pos_src[1] + self.pos_dst[1])/2]
            painter.drawText(midpoint[0]-text_width/2-20,midpoint[1]-text_height/2,text_width,text_height,Qt.AlignHCenter,self.text)