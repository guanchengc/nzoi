pantry = []

while 1:
    food = input().split()
    if food[0] == "D":
        break
    pantry.append(food)

outPut = [0, 0, 0, 0, 0, 0]
for foods in pantry:
    if foods[0] == "G":
        outPut[0] += int(foods[1])
    elif foods[0] == "C":
        outPut[1] += int(foods[1])
    elif foods[0] == "E":
        outPut[2] += int(foods[1])
    elif foods[0] == "P":
        outPut[3] += int(foods[1])
    elif foods[0] == "L":
        outPut[4] += int(foods[1])
    elif foods[0] == "S":
        outPut[5] += int(foods[1])

print(*outPut)