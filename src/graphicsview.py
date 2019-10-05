import sys
from PySide2 import QtCore, QtWidgets, QtGui
from pubsub import pub

from scene import GraphicsScene
from scenestate import GraphicsState
from scenelabel import SceneLabel

class GraphicsView(QtWidgets.QGraphicsView):

    def __init__(self):
        super(GraphicsView, self).__init__()
        self.setMouseTracking(True)
        #self.scene = QtWidgets.QGraphicsScene()
        self.scene = GraphicsScene()
        self.st = self.scene.addItem(QtWidgets.QGraphicsTextItem("Hello, world!"))
        self.setScene(self.scene)
        pub.subscribe(self.addState, "CONTROLLER_ADD_STATE")
        pub.subscribe(self.addTransition, "CONTROLLER_ADD_TRANSITION")

    #def mouseMoveEvent(self,event):
    #    pub.sendMessage("VIEW_MOUSE_MOVE", pos=event.pos())
    #    print("View Pos:"+str(event.pos()))

    def mousePressEvent(self, event):
        pub.sendMessage("VIEW_MOUSE_PRESS")
        super(GraphicsView,self).mousePressEvent(event)

    def addState(self,pos): # Add label object
        # circle = QtWidgets.QGraphicsEllipseItem(-50,-50,100,100)
        # circle.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 255), 1))
        # circle.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 0, 255)))
        # circle.setPos(pos)
        _gs = GraphicsState(pos)
        _sl = SceneLabel("Test")
        self.scene.addItem(_gs)
        _sl.setPos(pos)
        self.scene.addItem(_sl)


    def addTransition(self,pts):
        print(pts)
        _brush = QtGui.QBrush(QtGui.QColor(0, 255, 0, 255))
        _start = self.scene.addEllipse(-5,-5,10,10)
        _start.setBrush(_brush)
        _start.setPos(pts[0])