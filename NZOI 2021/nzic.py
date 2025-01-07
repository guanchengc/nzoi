n = int(input())
m = int(input())
queries = []
gets = []
for _ in range(m):
    a = input()
    if a[0] == "o":
        gets.append(int(a[2:]) - 1)
    else:
        queries.append(a)

competitors = ['o'] * n

def setStatus(q, c):
    for user in q:
        if c[int(user[2:]) - 1] == 'o':
            c[int(user[2:]) - 1] = "u"
        elif c[int(user[2:]) - 1] == 'u':
            c[int(user[2:]) - 1] = "o"
    return c

def output(c, g):

    for userNo in gets:
        if c[userNo] == "o":
            rank = userNo + 1 - c[0 : userNo + 1].count('u') 
            print(rank)
        elif c[userNo] == "u":
            print("UNOFFICIAL")
setStatus(queries, competitors)
output(competitors, gets)
        