def getInput():
    spells = list(map(int, input().split()))
    times = int(input())
    return [spells, times]

def createList(times):
    tempL = []
    tempL = [[None, None]] * times
    return tempL

def castSpell(spell, u, v):
    return [spell[0] * u + spell[1] * v, spell[2] * u + spell[3] * v]

def pops(lists, spell):
    items = [1, 1]
    lists[-1] = items.copy()
    for _ in range(len(lists) - 1):
        items = lists.pop()
        lists[-1] = castSpell(spell, items[0], items[1]).copy()
    return lists[-1]

def main():
    spell, no = getInput()
    no += 1
    lists = createList(no)
    print(*pops(lists, spell))

if __name__ == "__main__":
    main()