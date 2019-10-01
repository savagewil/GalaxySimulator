import math


def rounder(num):
    while not (math.pi * 2 >= num >= 0):
        if num < 0:
            num += math.pi * 2
        elif num > math.pi * 2:
            num -= math.pi * 2
    return num


class Vector:
    def __init__(self, **kwargs):
        self.dict = kwargs

    def getTheta(self):
        if "theta" in self.dict:
            return self.dict["theta"]
        else:
            r = (self.dict["i"] ** 2 + self.dict["j"] ** 2) ** (.5)
            c = rounder(math.acos(self.dict["i"] / r))
            s = rounder(math.asin(self.dict["j"] / r))
            s_ = rounder(math.pi - s)
            c_ = rounder(- c)
            if c == s or c == s_:
                return c
            else:
                return c_

    def getMagnitude(self):
        if "magnitude" in self.dict:
            return self.dict["magnitude"]
        else:
            return (self.dict["i"] ** 2 + self.dict["j"] ** 2) ** (.5)

    def getI(self):
        if "i" in self.dict:
            return self.dict["i"]
        else:
            i = self.dict["magnitude"] * math.cos(self.dict["theta"])
            self.dict["i"] = i
            return i

    def getJ(self):
        if "j" in self.dict:
            return self.dict["j"]
        else:
            i = self.dict["magnitude"] * math.sin(self.dict["theta"])
            self.dict["j"] = i
            return i

    def opposite(self):
        return Vector(i=-self.getI(), j=-self.getJ())

    def add(self, v):
        return Vector(i=self.getI() + v.getI(), j=self.getJ() + v.getJ())

    def subtract(self, v):
        return Vector(i=self.getI() - v.getI(), j=self.getJ() - v.getJ())

    def multiply(self, c):
        return Vector(i=self.getI() * c, j=self.getJ() * c)

    def __str__(self):
        return str(self.getI()) + "i " + str(self.getJ()) + "j"

##    def dot(self, v):
##        return self.getI() * v.getI() + 
