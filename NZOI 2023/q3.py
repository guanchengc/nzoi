import math
r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

grid = [r1, r2, r3]

maxi = 0
mini = math.inf
dif = 0

def checkGrid(grid):
    sum = grid[0][0] + grid[0][1] + grid[0][2]
    maxS = 0
    minS = math.inf
    for i in range(3):
        if grid[i][0] + grid[i][1] + grid[i][2] != sum:
            if grid[i][0] + grid[i][1] + grid[i][2] > maxS
            return False
        
    for j in range(3):
        if grid[0][j] + grid[1][j] + grid[2][j] != sum:
            return False
        
    if grid[0][0] + grid[1][1] + grid[2][2] == sum: 
        if grid[0][2] + grid[1][1] + grid[2][0] == sum:
            return True
        
    return False

def loopZeros(zeros, ind = 0):
    if ind >= len(zeros):
        if (checkGrid(grid)):
            for x in range(3):
                print(f"{grid[x][0]} {grid[x][1]} {grid[x][2]}")
            return True
        return False
    z = zeros[ind]
    for i in range(min((maxi - mini) * 2 + 1, 10000)):
        grid[z[0]][z[1]] = mini + i
        if (loopZeros(zeros, ind + 1)):
            return True
        
    grid[z[0]][z[1]] = 0
    return False




zeroPos = []

for row in range(len(grid)): 
    for element in range(len(grid[row])): 
        if int(grid[row][element]) > maxi:
            maxi = int(grid[row][element])

        if int(grid[row][element]) == 0:
            zeroPos.append([row, element])
        elif int(grid[row][element]) < mini:
            mini = int(grid[row][element])

loopZeros(zeroPos)