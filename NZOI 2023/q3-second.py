import math
class Circle():
    x = 0
    y = 0
    r = 0
    e = False
    
    def __init__(self, x, y, r, e = False) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.e = e
    
    def calcDist(self, x, y, r):
        
        return dist(self.x, self.y, x, y, self.r, r)


startX, startY, endX, endY = list(map(float, input().split()))
circ = []
n = int(input())
circ.append(Circle(endX, endY, 0, True))
for _ in range(n):
    x, y, r = list(map(float, input().split()))
    circ.append(Circle(x, y, r))

def dist(x1, y1, x2, y2, r1 = 0, r = 0):

    d = math.sqrt((x1-x2) * (x1-x2) + (y1 - y2) * (y1 - y2))

    if d > r + r1:
        return d - r - r1
    return 0


def main(circlList, startX, startY, dist = 0, r = 0, bestDist = math.inf):
    for ind in range(len(circlList)):
        circle = circlList[ind]
        if circle.e:
            bestDist = min(bestDist, circle.calcDist(startX, startY, r) + dist)
        else:
            tempL = circlList[:ind] + circlList[ind + 1:]
            di = circle.calcDist(startX, startY, r) + dist
            bestDist = min(bestDist, main(tempL, circle.x, circle.y, di, circle.r, bestDist))
    return bestDist
    



print(main(circ, startX, startY))