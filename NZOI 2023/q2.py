n = int(input())
a = 6
b = 0
stitcheLeft = 6
cuRow = 0
maxRow = 0
for _ in range(n):
    intru = input()
    id = intru[0]
    no = int(intru[1:])
    if stitcheLeft == 0:
        cuRow += 1
        stitcheLeft = b
        b = 0
    if id == "I":
        a += no - 1
        b += no
        stitcheLeft -= 1
    elif id == "D":
        a -= no - 1
        stitcheLeft -= no
        if stitcheLeft < 0:
            cuRow += 1
            stitcheLeft += b
            b = 1
        else:
            b += 1
    
    

    
print(a)
print(cuRow+1)

    