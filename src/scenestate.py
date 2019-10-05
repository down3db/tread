import sys
from PySide2 import QtCore, QtWidgets, QtGui
from pubsub import pub


class GraphicsState(QtWidgets.QGraphicsEllipseItem):

    def __init__(self,pos):
        super(GraphicsState, self).__init__(-50,-50,100,100)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 255), 1))
        self.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 0, 255)))
        self.setPos(pos)
