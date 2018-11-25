import math

class Pos2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcDistance(pos1, pos2):
    xx = math.fabs(pos1.x - pos2.x) * math.fabs(pos1.x - pos2.x)
    yy = math.fabs(pos1.y - pos2.y) * math.fabs(pos1.y - pos2.y)
    return math.sqrt(xx + yy)