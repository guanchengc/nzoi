import math

n = int(input())
expences = input().split()
sum = 0
for i in expences:
    sum += int(i)

closest = math.ceil(sum / n) * n
print(closest - sum)