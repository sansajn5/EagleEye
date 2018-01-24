import sys
from PyQt5.QtWidgets import QApplication
from helpers import Constants
CONST = Constants();
# TODO CHANGE TO PACEENV
print(sys.path)
sys.path.insert(0,CONST.PACEENV)

# Custom modules
from window import Window

def initialiseGui(const):
    app = QApplication(sys.argv)
    window = Window(sys.argv,const)
    sys.exit(app.exec_())

if __name__ == '__main__':
    CONST = Constants();
    initialiseGui(CONST)