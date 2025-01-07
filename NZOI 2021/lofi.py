noOfCust = int(input())
priceBid = []
for _ in range(noOfCust):
    priceBid.append(int(input()))

phonePrice = []
noOfPhone = int(input())
for _ in range(noOfPhone):
    phonePrice.append(int(input()))

priceBid.sort(reverse=True)
phonePrice.sort(reverse=True)

def getIncome(price, bids):
    income = 0
    a = 0
    b = a
    while True:
        if a >= len(bids) or b >= len(price):
            return income
        if bids[a] >= price[b]:
            income += price[b]
            a += 1
            b += 1
        else:
            b += 1

print(getIncome(phonePrice, priceBid))