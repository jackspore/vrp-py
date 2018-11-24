import math

def calcDistance(pos1, pos2):
    x2 = math.fabs(pos1.x - pos2.x) * math.fabs(pos1.x - pos2.x)
    y2 = math.fabs(pos1.y - pos2.y) * math.fabs(pos1.y - pos2.y)
    return math.sqrt(x2 + y2)