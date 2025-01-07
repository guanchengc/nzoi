people = {}
for i in range(20):
    room, person = input().split(" ")
    room = int(room)
    people[room] = person


evilcount = [0 for _ in range(20)]

for i in range(5):
    oe, n, letter = list(input().split(" "))
    for j in range(20):
        room = j + 101
        excluded = False
        if room % 2 == 0:
            if oe == "E":
                excluded = True
        else:
            if oe == "O":
                excluded = True
        if room % int(n) == 0:
            excluded = True
        if people[room][0] == letter:
            excluded = True
        if not excluded:
            evilcount[j] += 1

count = max(evilcount)

for i in range(20):
    if evilcount[i] == count:
        print(people[101 + i])