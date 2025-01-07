class house():
    visited = False
    position = 0
    def __init__(self, p):
        position = p

houses = []
for x in range(20):
    houses.append(house(x + 1))

inputs = input().split()
start = inputs[0]
instructions = inputs[1:]
currentHouse = houses[start]
output = []
illegal = False
for movement in instructions:
    currentHouse.visited = True
    if movement[0] == "U":
        currentHouse = houses[currentHouse.position + int(movement[1:])]
    elif movement[0] == "D":
        currentHouse = houses[currentHouse.position - int(movement[1:])]
    if currentHouse.visited:
        print("illegal")
        illegal = True
        break

if not illegal:
    for houseCheck in houses:
        if houseCheck.visited == False:
            output.append(houseCheck.position)

    print(*houseCheck)
