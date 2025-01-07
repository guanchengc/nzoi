canvas = []
h, w, n = map(int, input().split()) 
row = []

for _ in range(h):
 canvas.append([None] * w)


for _ in range(n):
    inpt = input().split()
    throwPosx = int(inpt[0])
    throwPosy = int(inpt[1])
    throwRad = int(inpt[2])
    throwCol = inpt[3]
    fill = [[],[]]
    fillax, fillay = max(throwPosx - throwRad, 0), max(throwPosy - throwRad, 0)

    fillbx, fillby = min(throwPosx + throwRad, w-1), min(throwPosy + throwRad, h-1)

    for y in range(fillax, fillbx + 1):    
        for x in range(fillay, fillby + 1):
            if y >= len(canvas[0]):
                continue
            if x >= len(canvas):
                continue
            canvas[x][y] = throwCol


cntCol = input()
count = 0
for row in range(h):
    count += canvas[row].count(cntCol)

print(count)