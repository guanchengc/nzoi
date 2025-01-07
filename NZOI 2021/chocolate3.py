import operator
import math

def checkIfCanceled(lst, cap):
    leftReq = 0
    rightReq = 0
    totalReq = leftReq + rightReq
    for children in lst:
        if children.left == -1:
            rightReq += children.cups
        elif children.right == -1:
            leftReq += children.cups
        else:
            totalReq += children.cups
    
    if leftReq > cap[0] or rightReq > cap[1] or totalReq > cap[0] + cap[1]:
        return True
    
    return False

def findMaxHappiness(lst, cap):
    hap = 0
    left = []
    right = []
    for children in lst:
        if children.left == -1:
            hap += children.right
            cap[0] -= children.cups
        elif children.right == -1:
            hap += children.left
            cap[1] -= children.cups
        else:
            left.append(children)
            right.append(children)
        
    while 1:
        left.sort(key=operator.attrgetter("lAvg"), reverse=True)
        right.sort(key=operator.attrgetter("rAvg"), reverse=True)
        lDif = left[0].lAvg - left[1].lAvg
        rDif = right[0].rAvg - right[1].rAvg
        if lDif > rDif:
            hap += left[0].left
            left[0].lAvg = math.inf
            left[0].rAvg = math.inf
            cap[0] -= left[0].cups
        else:
            hap += right[0].right
            right[0].lAvg = math.inf
            right[0].rAvg = math.inf
            cap[0] -= right[0].cups

        if math.isinf(left[0].lAvg):
            break

    return hap

class child():
    left = 0
    right = 0
    cups = 0
    lAvg = 0
    rAvg = 0

    def __init__(self, c, l, r):
        self.left = l
        self.right = r
        self.cups = c
        self.lAvg = l/c
        self.rAvg = r/c        

def main():
    capacity = list(map(int, input().split()))
    amtPeople = int(input())
    preference = []


    for _ in range(amtPeople):
        newItem = list(map(int, input().split()))

        preference.append(child(newItem[0], newItem[1], newItem[2]))

    if checkIfCanceled(preference, capacity):
        print("Camp is cancelled")
    else:
        print(findMaxHappiness(preference, capacity))

def test():
    assert findMaxHappiness([
        child(3, 1, 6),
        child(2, 6, 4),
        child(2, 5, -1)
    ], [4, 6]) == 1788
    print("hi")

test()