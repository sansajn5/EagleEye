import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Class representing gui initializer
class Window(QMainWindow):

    # Constructor calling super class and setting paramters
    def __init__(self, args, constants):
        super().__init__()
        self.args = args
        self.CONST = constants
        self.initiliseUI()

    # Defining window parameters
    def initiliseUI(self):

        self.createActions()
        self.statusBar()
        self.createMenuBar()
        self.createToolBar()

        # TODO set size
        self.setGeometry(300, 200, 1500, 900)
        self.setWindowTitle(self.CONST.TITLE)
        self.show()

    # Initializing actions
    def createActions(self):
        ### Menu bar ###
        ##TODO Set icons
        self.exitActMB = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitActMB.setShortcut('Ctrl+Q')
        self.exitActMB.setStatusTip('Exit application')
        self.exitActMB.triggered.connect(qApp.quit)

        ###Toolbar ###
        ##TODO Set icons
        self.exitActTB = QAction(QIcon('exit24.png'), 'Exit', self)
        self.exitActTB.setShortcut('Ctrl+Q')
        self.exitActTB.triggered.connect(qApp.quit)


    # Initializing menu bar
    # Allowing easy customization
    def createMenuBar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.exitActMB)

    # Initializing tool bar
    # Allowing easy customization
    def createToolBar(self):
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exitActTB)
