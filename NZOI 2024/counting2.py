num = input()
sum = 0
multiplyier = 0
for i in range(len(num)):
    digit = int(num[len(num) - i - 1])
    power = i
    sum += multiplyier * digit
    if digit == 3:
        sum += int("0" + num[len(num) - i:]) + 1
    elif digit > 3:
        sum += pow(10, power)
    multiplyier *= 10
    multiplyier += pow(10, power)

print(sum)