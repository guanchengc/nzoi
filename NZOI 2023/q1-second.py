n = int(input())
maHill = -1
sums = 0

for i in range(n):
    a = int(input())
    if a >= 0:
        sums += a
    else:
        if sums > 0:
            maHill = max(maHill, sums)
        sums = 0

maHill = max(maHill, sums)
print(maHill)