import sys
from PySide2 import QtCore, QtWidgets, QtGui
from graphicsview import GraphicsView
from pubsub import pub

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.textEdit = QtWidgets.QTextEdit()
        self.view = GraphicsView()
        self.vSplitter = QtWidgets.QSplitter()
        self.vSplitter.addWidget(self.view)
        self.vSplitter.addWidget(self.textEdit)
        self.vSplitter.setOrientation(QtCore.Qt.Vertical)
        self.setCentralWidget(self.vSplitter)

        self.createActions()
        self.createMenus()

    def createActions(self):
        self.addStateAction = QtWidgets.QAction(
                 "Add State",
                self, shortcut="Ctrl+E", statusTip="Add a State",
                triggered=self.addState)

        self.addTransitionAction = QtWidgets.QAction(
                "Add Transition",
                self, shortcut="Ctrl+T", statusTip="Add a Transition",
                triggered=self.addTransition
                )

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        #self.fileMenu.addAction(self.exitAction)

        self.toolsMenu = self.menuBar().addMenu("&Tools")
        self.toolsMenu.addAction(self.addStateAction)
        self.toolsMenu.addAction(self.addTransitionAction)


    def addState(self):
        pub.sendMessage("MAINWINDOW_ADD_STATE")

    def addTransition(self):
        pub.sendMessage("MAINWINDOW_ADD_TRANSITION")
