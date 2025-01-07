#you are trying to reach a number, n, and each numberpad on the calculator gives a shock level of s, different for each button, and + * and = can be only typed once. find the lease amount of shock needed to get the number you wanted

import math

def inputs():
    numDisplay = int(input())
    hurtvalue = list(map(int, input().split()))
    hurtvalueKeys = list(map(int, input().split()))
    return [numDisplay, hurtvalue, hurtvalueKeys]

def minus(a, b):
    c = a - b
    if c == 0:
        return ""

    return abs(c)

def minmax(objective, hurt, hurtK, possib, least, f):
    possibles = []
    for a in range(1, math.ceil(math.sqrt(objective))):
        b = int(math.ceil(objective / a)) * a
        possibles.append(str(a) + '*' + str(int(math.ceil(objective / a))) + str(minus(b, objective)))
        possibles.append(str(a) + '*' + str(int(math.floor(objective / a))) + "+" + str(objective - int(math.floor(objective / a)) * a))

    for a in range(1, objective // 2):
        possibles.append(str(a)+"+"+ str(objective - a))

    possibles.append(str(objective))

    possibles.sort()
    hurts = []
    for x in possibles:
        hurtC = 0
        for y in x:
            if y == "+":
                hurtC += hurtK[0]
            elif y == "*":
                hurtC += hurtK[1]
            else:
                hurtC += hurt[int(y)]
        hurts.append(hurtC)

    least = math.inf
    for a in hurts:
        if a < least:
            least = a


    return least + hurtK[-1]
        



a, b, c = inputs()
print(minmax(a, b, c, "0", 0, False))