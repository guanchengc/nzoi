x, y, a, b = map(int, input().split())

triala = (x//a) * (y//b)
trialb = (x//b) * (y//a)

print(max(triala, trialb))