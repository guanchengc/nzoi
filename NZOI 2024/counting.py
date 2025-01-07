#find the amount 3s in the range of a given number eg 3 = 1, 13 = [3, 13] = 2 and 33 counts as 2

def counting(num):
    countNum = 0
    a = 3
    for x in range(0, findPower(num) + 1):
        if num - a < 0:
            break
        countNum += ((num - a)//pow(10, x+1)+1)*pow(10, x)
        a = a * 10 + 9
    
    countNum += findRest(num)
    return countNum

def findRest(num):
    n = 0
    if str(num)[0] == '3' and len(str(num)) != 1:
        n = num - 3 * pow(10, findPower(num)) + 1
    
    if len(str(num)) != 1:
        return n + findRest(int(str(num)[1:]))

    return 0

def count(num):
    countNum = 0
    for x in range(len(str(num))):
        if x == 0:
            if int(str(num)[x]) >= 3:
                countNum += 1
        else:
            a = 0
            if int(str(num)[x]) >= 3:
                a = 1
            countNum += a * pow(10, x) + int(str(num)[x]) * pow(10, x-1)

    return countNum

        

def findPower(num):
    return len(str(num)) - 1

def test():
    assert counting(3) == 1
    assert counting(13) == 2
    assert counting(33) == 8
    assert counting(333) == 102
    
print(counting(int(input())))