#there are 2 coco machines, a, b, N numbers of student will take a drink from them. if the student gets a drink, he will respond his happy level of l for left and r for right, if he hates l, the input l will be -1, same for r, if the cups are not enough for everyone, it will output camp is canceled

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
    if count > cups[1]:
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

def solutiona(students):
    happy = 0
    students.sort(key=lambda x: x.left)
    tempL = students
    for a in students[0:avaliable[0]]:
        if a.left == -1:
            break
        happy += a.left
        tempL.pop(0)
        if avaliable[0] == 0:
            break
    
    students = tempL
    students.sort(key=lambda x: x.right)
    tempL = students

    for a in students[0:avaliable[1]]:
        if a.right == -1:
            break
        happy += a.right
        tempL.pop(0)
        if avaliable[0] == 0:
            break

    return happy

def solutionb(students):
    happy = 0
    students.sort(key=lambda x: x.right)
    tempL = students

    for a in students[0:avaliable[1]]:
        if a.right == -1:
            break
        happy += a.right
        tempL.pop(0)
        if avaliable[0] == 0:
            break

    students = tempL
    students.sort(key=lambda x: x.left)
    tempL = students
    for a in students[0:avaliable[0]]:
        if a.left == -1:
            break
        happy += a.left
        tempL.pop(0)
        if avaliable[0] == 0:
            break
    

    return happy

if findCancel(avaliable, students) == False:
    print(max(solutiona(students), solutionb(students)))