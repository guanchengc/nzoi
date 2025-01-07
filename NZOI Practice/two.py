n = int(input())

text = []

if n % 2 == 0:
    a = n // 2

    for i in range(n - a):
        text.append(a)
        text.append(n // 2 + a)
        a -= 1
else:
    text.append(1)
    a = (n - 1) // 2
    for i in range(n - 1 - a):
        text.append(a + 1)
        text.append(n//2 + a + 1)
        a -= 1

print(*text)