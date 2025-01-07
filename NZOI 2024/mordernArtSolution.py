H, W, N = map(int, input().split())
# create an empty canvas
canvas = []
for _ in range(H):
 canvas.append([None] * W)
# paint the canvas
for _ in range(N):
 ln = input().split()
 # convert first 3 bits to integers
 a, b, spread = map(int, ln[:3])
 colour = ln[3]
 # upper left corner of the painted square
 x = max(a - spread, 0)
 y = max(b - spread, 0)
 # lower right corner of the painted square
 u = min(a + spread, W - 1)
 v = min(b + spread, H - 1)
 # fill in between the two coordinates
 for i in range(x, u + 1):
    for j in range(y, v + 1):
        canvas[j][i] = colour
# count the number of coloured cells
col = input().strip()
num_col = 0
for i in range(H):
 num_col += canvas[i].count(col)
print(num_col)
