import numpy as np
import cv2
import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Trke')
    w.setGeometry(100,100,700,400)
    p = QtWidgets.QPushButton(w)
    p.setText('Play >')
    p.move(300,350)
    
    s = QtWidgets.QPushButton(w)
    s.setText('Stop x')
    s.move(380,350)
    
    
    w.show()
    sys.exit(app.exec_())

window()

