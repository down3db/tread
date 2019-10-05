import sys
from PySide2 import QtCore, QtWidgets, QtGui
from pubsub import pub
from state import State

# Does a lot of listening, and then sends some events
class Controller(QtCore.QObject):
    def __init__(self):
        self.pos = None # Mouse Position in View
        self.adding_state = False
        self.adding_transition = False
        #pub.subscribe(self.mouseMove, "VIEW_MOUSE_MOVE")
        pub.subscribe(self.addingState, "MAINWINDOW_ADD_STATE")
        pub.subscribe(self.addingTransition, "MAINWINDOW_ADD_TRANSITION")
        pub.subscribe(self.mousePress, "VIEW_MOUSE_PRESS")
        pub.subscribe(self.sceneMouseMove, "SCENE_MOUSE_MOVE")
        self.stateList = []

    # From the View
    def sceneMouseMove(self,pos):
        self.pos = pos

    def mousePress(self):
        if self.adding_state == True:
            state = State()
            self.stateList.append(state)
            pub.sendMessage("CONTROLLER_ADD_STATE", pos=self.pos)
            self.adding_state = False

        if self.adding_transition == True:
            self.tmp_transition_pts.append(self.pos) # Since we always have the mouse's location in the scene through controller's pos
            if len(self.tmp_transition_pts)==3:
                self.adding_transition = False
                pub.sendMessage("CONTROLLER_ADD_TRANSITION", pts = self.tmp_transition_pts)
                self.tmp_transition_pts = []


    # From the MainWindow
    def addingState(self):
        self.adding_state = True

    def finalizeAddState(self):
        pass

    def addingTransition(self):
        self.adding_transition = True
        self.tmp_transition_pts = []
