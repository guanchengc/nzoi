

def checkDupe(l):
    dupes = []
    for index in range(len(l)):
        num = l[index]
        if num in l[:index] + l[index+1:]:
            dupes.append(num)
    
    return list(set(dupes))

def loop(listOfCards, counter = 0):
    if len(listOfCards) < 3:
        return counter, listOfCards
    a = len(listOfCards)
    for i in range(a - 2):
        if listOfCards[i] == listOfCards[i+1] and listOfCards[i+1] == listOfCards[i+2]:
            listOfCards.pop(i)
            listOfCards.pop(i)
            listOfCards.pop(i)
            counter += 1
            return loop(listOfCards, counter)
        if listOfCards[i] + 1 in listOfCards and listOfCards[i] + 2 in listOfCards:
            n = listOfCards[i]
            listOfCards.remove(n)
            listOfCards.remove(n + 1)
            listOfCards.remove(n + 2)
            counter += 1
            return loop(listOfCards, counter)
    
    return counter, listOfCards


def findWin(listOfCards, counter = 0):
    a = len(listOfCards)
    b = None
    if a % 3 == 2:
        b = checkDupe(listOfCards)
    
    if b:
        for num in b:
            copyL = listOfCards.copy()
            copyL.remove(num)
            copyL.remove(num)
            c, l = loop(copyL, counter)
            if len(l) == 0:
                return c, [num, num]
            
        return 0, [1, 1]
    else:
        c, l = loop(listOfCards, counter)
        return c, l

input()
p = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
counter = 0
comp = False
simple = False
pa = False
ca = False
ba = False
if len(p) >= 1:
    if max(p) < 9:
        if min(p) > 1:
            pa = True
else: 
    pa = True
            
if len(b) >= 1:
    if max(b) < 9:
        if min(b) > 1:
            ba = True
else:
    ba = True
            
if len(c) >= 1:
    if max(c) < 9:
        if min(c) > 1:
            ca = True
else:
    ca = True

if pa and ca and ba: 
    simple = True

tp = p.copy()
tb = b.copy()
tc = c.copy()
x, p = findWin(p)
counter += x
x, b = findWin(b)
counter += x
x, c = findWin(c)
counter += x
if counter == 4:

    if len(p) == 2:
        if p[0] == p[1]:
            comp = True
        
    if len(b) == 2:
        if b[0] == b[1]:
            comp = True
        
    if len(c) == 2:
        if c[0] == c[1]:
            comp = True

if simple and comp:
    print("WIN")
elif simple:
    print("SIMPLE")
elif comp:
    print("COMPLETE")
else:
    print("SAD")