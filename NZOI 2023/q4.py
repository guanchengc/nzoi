friends = []
n = int(input())

class friended():
    A = 0
    B = 0
    factorDif = 0
    def __init__(self, p1, p2) -> None:
        self.A = p1
        self.B = p2
        self.factorDif = self.B / self.A
    
    def __str__(self) -> str:
        return str(self.A)

for _ in range(n):
    bond = list(map(int, input().split()))
    friends.append(friended(bond[0], bond[1]))

friends.sort(key= lambda x : (x.factorDif, x.A))

a = ""
for i in friends:
    a += str(i) + " "
print(a)