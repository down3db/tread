import sys
from PySide2 import QtCore, QtWidgets, QtGui
from pubsub import pub

class SceneLabel(QtWidgets.QGraphicsTextItem):
    # C:\Program Files (x86)\Python37-32\Lib\site-packages\PySide2\examples\widgets\graphicsview\diagramscene\diagramscene.py

    lostFocus = QtCore.Signal(QtWidgets.QGraphicsTextItem)
    selectedChange = QtCore.Signal(QtWidgets.QGraphicsItem)

    def __init__(self,text):
        super(SceneLabel, self).__init__(text)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemSelectedChange:
            self.selectedChange.emit(self)
        return value

    def focusOutEvent(self, event):
        self.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lostFocus.emit(self)
        super(SceneLabel, self).focusOutEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.textInteractionFlags() == QtCore.Qt.NoTextInteraction:
            self.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        super(SceneLabel, self).mouseDoubleClickEvent(event)