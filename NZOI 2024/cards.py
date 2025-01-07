def getInputes():
    num = input()
    card = input()
    return [card, num]

def compare(card):
    if card == "hearts":
        return 0
    elif card == "diamonds":
        return 1
    elif card == "clubs":
        return 2
    elif card == "spades":
        return 3

def compareNum(num):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return 12 - order.index(num)

def main():
    card = getInputes()
    a = compare(card[0]) * 13
    b = compareNum(card[1])
    print(int(a) + int(b))

main()
    