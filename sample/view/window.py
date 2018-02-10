import sys
from distutils.extension import read_setup_file

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np
import cv2
import numpy as np
import imutils
import Person
import time

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


    def calculate(self,niz):
        temp = []
        person1 = niz[0]
        person2 = niz[1]
        person3 = niz[2]
        person4 = niz[3]
        p1 = person1.getTop()[0][1]
        p2 = person2.getTop()[0][1]
        p3 = person3.getTop()[0][1]
        p4 = person4.getTop()[0][1]
        temp.append(p1)
        temp.append(p2)
        temp.append(p3)
        temp.append(p4)
        results = sorted(temp);
        if(p1 == results[0]):
            print('Racer in first lane is winner')
        if(p1 == results[1]):
            print('Racer in first lane won second place')
        if(p1 == results[2]):
            print('Racer in first lane won third place')
        if(p1 == results[3]):
            print('Racer in fist lane finished last')

        if (p2 == results[0]):
            print('Racer in second lane is winner')
        if (p2 == results[1]):
            print('Racer in second lane won second place')
        if (p2 == results[2]):
            print('Racer in second lane won third place')
        if (p2 == results[3]):
            print('Racer in second lane finished last')

        if (p3 == results[0]):
            print('Racer in third lane is winner')
        if (p3 == results[1]):
            print('Racer in third lane won second place')
        if (p3 == results[2]):
            print('Racer in third lane won third place')
        if (p3 == results[3]):
            print('Racer in third lane finished last')

        if (p4 == results[0]):
            print('Racer in fourth lane is winner')
        if (p4 == results[1]):
            print('Racer in fourth lane won second place')
        if (p4 == results[2]):
            print('Racer in fourth lane won third place')
        if (p4 == results[3]):
            print('Racer in fourth lane finished last')

    # TODO Make function that will play a video
    def play(self):
        # print(self.filePath[0])
        cap = cv2.VideoCapture('/home/sansajn/Downloads/trke/trka1.mov')
        cnt_up = 0
        cnt_down = 0
        niz = [];

        #get width of screen
        w = cap.get(3)
        #get height of screen
        h = cap.get(4)

        #size of screen
        frameArea = h * w
        areaMin = frameArea / 250
        areaMax = frameArea / 100

        #setting line for finish and limit for realaseing memory allocation
        #line_finish = int(5 * (w / 6 ));
        #line_limit = int(3 * (w/6));

        #finish line vortex
        pt1 = [263, h/1.35];
        pt2 = [235, h];
        pts_L1 = np.array([pt1, pt2],np.int32)
        pts_L1 = pts_L1.reshape((-1, 1, 2))

        #limit line vortex
        pt3 = [260, 810];
        pt4 = [235, h];
        pts_L2 = np.array([pt3, pt4],np.int32)
        pts_L2 = pts_L2.reshape((-1, 1, 2))

        #first line
        pt5 = [0, 830];
        pt6 = [w, 680];
        pts_L3 = np.array([pt5, pt6], np.int32)
        pts_L3 = pts_L3.reshape((-1, 1, 2))

        # second line
        pt7 = [0, 870];
        pt8 = [w, 710];
        pts_L4 = np.array([pt7, pt8], np.int32)
        pts_L4 = pts_L4.reshape((-1, 1, 2))


        #background substractor
        fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

        #kernel parametars
        kernelOp = np.ones((3, 3), np.uint8)
        kernelOp2 = np.ones((5, 5), np.uint8)
        kernelCl = np.ones((11, 11), np.uint8)

        # Variables
        font = cv2.FONT_HERSHEY_SIMPLEX
        persons = []
        pid = 1

        while (cap.isOpened()):
            ret, frame = cap.read()

            #applying substraction
            fgmask = fgbg.apply(frame)
            fgmask2 = fgbg.apply(frame)

            # fgmask2 = cv2.erode(fgmask2, kernel, iterations=1)
            try:
                #isolating object
                ret, imBin = cv2.threshold(fgmask, 240, 255, cv2.THRESH_BINARY)
                ret, imBin2 = cv2.threshold(fgmask2, 240, 255, cv2.THRESH_BINARY)
                #opening same as erode
                mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
                mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
                #closing same as dilate
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelCl)
                mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
            except:
                print('Positions after race')
                self.calculate(niz)
                break

            # Tracking object with contours
            _, contours0, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours0:
                area = cv2.contourArea(cnt)
                if area > areaMin:

                    M = cv2.moments(cnt)
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    x, y, w, h = cv2.boundingRect(cnt)

                    new = True
                    # if cy in range(up_limit, down_limit):
                    for i in persons:
                        # checking if person already was detected
                        if abs(cx - i.getX()) <= w and abs(cy - i.getY()) <= h:
                            new = False
                            #update movement of object
                            i.updateCoords(cx, cy)

                            if(x<263):
                                i.setTop(x,y+h)
                                if i not in niz:
                                    niz.append(i)

                    if new == True:
                        p = Person.MyPerson(pid, cx, cy)
                        persons.append(p)
                        pid += 1

                    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                    img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    #cv2.drawContours(frame, cnt, -1, (0,255,0), 3)


            for i in persons:
                cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

            str_up = 'UP: ' + str(cnt_up)
            str_down = 'DOWN: ' + str(cnt_down)
            frame = cv2.polylines(frame, [pts_L1], False, (255, 0, 0), thickness=2)
            frame = cv2.polylines(frame, [pts_L2], False, (0, 0, 255), thickness=2)
            frame = cv2.polylines(frame, [pts_L3], False, (0, 0, 255), thickness=2)
            frame = cv2.polylines(frame, [pts_L4], False, (0, 0, 255), thickness=2)
            cv2.putText(frame, str_up, (10, 40), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, str_up, (10, 40), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

            cv2.imshow('Frame', frame)
            #cv2.imshow('Mask',mask)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                print(niz)
                break

        cap.release()
        cv2.destroyAllWindows()