import math

class student():
    left = 0
    right = 0
    cups = 0
    def __init__(self, l, r, c):
        self.left = l
        self.right = r
        self.cups = c

    def attribute(self):
        return [self.left, self.right, self.cups]


avaliable = list(map(int, input().split()))
students = []
for x in range(int(input())):
    stud = list(map(int, input().split()))
    for _ in range(stud[0]):
        students.append(student(stud[1], stud[2], 1))

def findCancel(cups, students):
    count = 0
    for studentt in students:
        if studentt.left == -1:
            count += 1 * studentt.cups
    if count > 0:
        print('Camp is cancelled')
        return True
    count = 0
    for studentt in students:
        if studentt.right == -1:
            count += 1 * studentt.cups
    if count > cups[0]:
        print('Camp is cancelled')
        return True

    cupsNeeded = 0
    for a in students:
        cupsNeeded += a.cups
    if cupsNeeded > cups[0] + cups[1]:
        print('Camp is cancelled')
        return True

    return False


if findCancel(avaliable, students) == False:
    happy = 0
    for x in students:
        happy += x.left
    print(happy)