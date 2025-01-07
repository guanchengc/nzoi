small = int(input())
medium = int(input())
large = int(input())

smallLi = ''
mediumLi = ''
largeLi = ''

longest = max(small, medium, large)

def setArray(longest, amount, lists, currentSize):
    longSide = longest
    lists = currentSize * amount
    longSide -= amount
    side = 1
    while longSide > 0:
        if side == 1:
            lists += '_'
            longSide -= 1
            side = 0
        else:
            lists = '_' + lists
            longSide -= 1
            side = 1

print(setArray(longest, large, largeLi, 'L'))
print(setArray(longest, medium, mediumLi, 'M'))
print(setArray(longest, small, smallLi, 'S'))