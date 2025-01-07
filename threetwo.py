n, a = map(int, input().split())
squares = []
covered = []

length = a * 2 + 1

def asserting(k):
    return int(k) - a

for _ in range(n):
    squares.append(list(map(asserting, input().split())))


covered = 0
startings = []
for square in squares:
    startx = square[0]
    endx = square[0] + a * 2
    starty = square[1]
    endy = square[1] + a * 2
    if startx < 0 and starty < 0:
        covered += startx * length
        covered += starty * length
        covered += starty ** 2
    elif startx < 0:
        covered += startx * length
    elif starty < 0:
        covered += starty * length
    covered += (length) ** 2
    for other in startings:
        ah = other[0] + length
        aw = other[1] + length
        if startx < ah:
            if starty < aw:
                covered -= (aw - startx) * (aw - starty)

    startings.append([startx, starty])


    

print(covered)