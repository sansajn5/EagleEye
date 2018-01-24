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
        self.buttons()

        self.setGeometry(300, 200, 1500, 900)
        self.setWindowTitle(self.CONST.TITLE)
        self.show()

    # Initializing actions
    def createActions(self):
        ### Menu bar ###
        ##TODO Set icons
        self.exitActMB = QAction(QIcon('/images/exit.png'), '&Exit', self)
        self.exitActMB.setShortcut('Ctrl+Q')
        self.exitActMB.setStatusTip('Exit application')
        self.exitActMB.triggered.connect(qApp.quit)

        ###Toolbar ###
        ##TODO Set icons
        self.exitActTB = QAction(QIcon('/images/exit.png'), 'Exit', self)
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

    # Initializing file chooser
    def fileChooser(self):
        self.filePath = QFileDialog.getOpenFileName(self, CONST.FILE_SELECTION , CONST.FILE_CHOOSER_DEFAULT)

    # Initializing buttons
    def buttons(self):
        # button for choosing video
        self.chooseButton = QPushButton('Browse', self)
        self.chooseButton.move(30, 50)
        self.chooseButton.clicked.connect(self.fileChooser)

        # play and stop buttons
        self.playButton = QPushButton('Play', self)
        self.playButton.move(30, 100)
        self.playButton.clicked.connect(self.play)

        self.pausePlayButton = QPushButton('Pause/Play', self)
        self.pausePlayButton.move(600, 720)

    # TODO Make function that will play a video
    def play(self):
        print(self.filePath[0])