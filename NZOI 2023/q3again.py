import math
r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

grid = [r1, r2, r3]
zeroPos = []

for row in range(len(grid)): 
    for element in range(len(grid[row])): 

        if grid[row][element] == 0:
            zeroPos = [row, element]

grid[zeroPos[0]][zeroPos[1]] = grid[zeroPos[0] - 1][0] + grid[zeroPos[0] - 1][1] + grid[zeroPos[0] - 1][2] - grid[zeroPos[0] - 1][zeroPos[1]] - grid[zeroPos[0] - 2][zeroPos[1]]

for x in range(3):
    print(f"{grid[x][0]} {grid[x][1]} {grid[x][2]}")