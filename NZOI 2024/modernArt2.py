class throw():
    posX = 0
    posY = 0
    col = ""
    radius = 0
    w = 0
    h = 0
    def __init__(self, x, y, colour, rad, h, w):
        self.posX, self.posY, self.col, self.radius = x, y, colour, rad
        self.w, self.h = w, h

    def getSquares(self):
        squares = []
        for x in range(self.posX - self.radius, self.posX + self.radius + 1):
            for y in range(self.posY - self.radius, self.posY + self.radius + 1):
                if x < 0 or x >= self.w or y < 0 or y >= self.h:
                    continue
                squares.append((x, y))
        return squares


def inputAttr():
    height, width, no = map(int, input().split())
    throws = []
    for _ in range(no):
        inpt = input().split()
        throws.append(throw(int(inpt[0]), int(inpt[1]), inpt[3], int(inpt[2]), height, width))

    colToFindOut = input()
    return [height, width, no, throws, colToFindOut]

def findNoSquares(throws, colToFindOut, h, w):
    sqares = []
    firstReached = False


    for throwItem in throws:

        if throwItem.col == colToFindOut:
            firstReached = True
        if firstReached == False:
            continue
        if throwItem.col == colToFindOut:
            sqares = set(sqares).union(set(throwItem.getSquares()))
        else:
            sqares = set(sqares).difference(set(throwItem.getSquares()))
    
    return sqares

def main():
    h, w, n, throws, colToFindOut = inputAttr()
    squaresCovered = findNoSquares(throws, colToFindOut, h, w)
    print(len(squaresCovered))
     
def test():
    a = throw(0, 0, "a", 1, 1, 1)
    b = throw(0, 0, "a", 1, 1, 1)
    assert a == b
    print(set([(3, 3), (3, 3)]))                              

if __name__ == "__main__":
    main()
