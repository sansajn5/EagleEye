import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np
import cv2
import numpy as np
import imutils


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

        self.setGeometry(100, 500, 400, 200)
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
        self.filePath = QFileDialog.getOpenFileName(self, self.CONST.FILE_SELECTION, self.CONST.FILE_CHOOSER_DEFAULT)
        # print(self.filePath)

    # Initializing buttons
    def buttons(self):
        # button for choosing video
        self.chooseButton = QPushButton('Browse', self)
        self.chooseButton.move(150, 50)
        self.chooseButton.clicked.connect(self.fileChooser)

        # play and stop buttons
        self.playButton = QPushButton('Play', self)
        self.playButton.move(150, 100)
        self.playButton.clicked.connect(self.play)

    # TODO Make function that will play a video
    def play(self):
        # print(self.filePath[0])
        camera = cv2.VideoCapture('/home/sansajn/Downloads/trke/trka3.mov')
        # camera = cv2.VideoCapture(self.filePath[0])
        # initialize the first frame in the video stream
        firstFrame = None

        # loop over the frames of the video
        while True:
            # grab the current frame and initialize the occupied/unoccupied
            # text
            (grabbed, frame) = camera.read()
            text = "Unoccupied"

            # if the frame could not be grabbed, then we have reached the end
            # of the video
            if not grabbed:
                break

            # resize the frame, convert it to grayscale, and blur it
            frame = imutils.resize(frame, width=1000)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (51, 51), 0)
            cv2.imshow("Pace", gray)
            # if the first frame is None, initialize it
            if firstFrame is None:
                firstFrame = gray
                continue

            # compute the absolute difference between the current frame and
            # first frame
            frameDelta = cv2.absdiff(firstFrame, gray)

            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

            # dilate the thresholded image to fill in holes, then find contours
            # on thresholded image
            thresh = cv2.dilate(thresh, None, iterations=2)
            (_ ,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

            # loop over the contours
            for c in cnts:
                # compute the bounding box for the contour, draw it on the frame,
                # and update the text
                print(c)
                (x, y, w, h) = cv2.boundingRect(c)

                if(h <8 and w < 5):
                    cv2.rectangle(frame, (x, y), (x + w, y + h ), (123, 132, 123), 2)
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h ), (0, 255, 255), 2)
                    # print(x)
                    # print(y)
                    # print(w)
                    # print(h)
                    # print('--------------------------------------------------')
                    # print('--------------------------------------------------')
                text = "Occupied"

            # draw the text and timestamp on the frame
            cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # show the frame and record if the user presses a key
            cv2.imshow("Security Feed", frame)
            cv2.imshow("Thresh", thresh)
            cv2.imshow("Frame Delta", frameDelta)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key is pressed, break from the lop
            if key == ord("q"):
                break

        # cleanup the camera and close any open windows
        camera.release()
        cv2.destroyAllWindows()