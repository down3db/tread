import sys
from PySide2 import QtCore, QtWidgets, QtGui
from mainwindow import MainWindow
from controller import Controller

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    controller = Controller()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())