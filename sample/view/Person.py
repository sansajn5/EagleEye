from random import randint

class MyPerson:
    tracks = []

    def __init__(self, i, xi, yi):
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        self.R = randint(0, 255)
        self.G = randint(0, 255)
        self.B = randint(0, 255)
        self.done = False
        self.state = '0'
        self.top = []

    def getRGB(self):
        return (self.R, self.G, self.B)

    def getTracks(self):
        return self.tracks

    def getId(self):
        return self.i

    def getState(self):
        return self.state

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setTop(self,xn,yn):
        self.top.append([xn,yn])

    def getTop(self):
        return self.top

    def updateCoords(self, xn, yn):
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def setDone(self):
        self.done = True

    def getDone(self):
        return self.done;
