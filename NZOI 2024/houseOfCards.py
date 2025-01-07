N = int(input())
cards = 0
for num in range(N):
    cards += num
    cards += (num + 1) * 2

print(cards)