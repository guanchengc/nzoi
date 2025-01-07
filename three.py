n, a = map(int, input().split())
squares = []
covered = []

for _ in range(n):
    squares.append(list(map(int, input().split())))


length = a * 2 + 1
sub = 0
total = n * length ** 2
for square in squares:
    counter = 0
    accounted = False
    for i in range(length):
        posx = square[0] - a + i
        if posx < 0:
            if not accounted:
                sub += posx * length * 2 
                sub += posx ** 2
                accounted = True
            continue
        if posx in covered:
            counter += 1
        else:
            if counter:
                sub -= counter ** 2
                counter = 0
            covered.append(posx)
    
    

print(total + sub)