import sys
from PySide2 import QtCore, QtWidgets, QtGui
from pubsub import pub

class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(GraphicsScene, self).__init__()
        self.setSceneRect(0,0,1024,1024)

    def mouseMoveEvent(self,event):
        pub.sendMessage("SCENE_MOUSE_MOVE", pos=event.scenePos().toPoint())
        super(GraphicsScene,self).mouseMoveEvent(event)