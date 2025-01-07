import logging


logging.basicConfig(level=logging.DEBUG)
duckTotal = int(input())
costOfT = int(input()) / 2
costOfTr = int(input()) / 3

def findCheap(two, three, amount):
    t = 0
    tr = 0
    rest = 0
    costs = []
    if (three < two):
        tr = amount // 3
        while True:
            if (tr < 0):
                break
            rest = amount - tr * 3
            if (rest % 2 == 0):
                t = rest / 2
                logging.debug(t)
                logging.debug(tr)
                costs.append(tr * 3 * three + t * 2 * two)
                tr -= 1
                break
            else:
                tr -= 1
                continue
    else:
        t = amount // 2
        while True:
            if (t < 0):
                break
            rest = amount - t * 2
            if (rest % 3 == 0):
                tr = rest / 3
                logging.debug(t)
                logging.debug(tr)
                costs.append(tr * 3 * three + t * 2 * two)
                t -= 1
                break
            else:
                t -= 1
                continue
    
    costs.sort()
    return int(costs[0])

print(findCheap(costOfT, costOfTr, duckTotal))