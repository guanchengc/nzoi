class person():
    parent1 = None
    parent2 = None
    def __init__(self, p1, p2):
        self.parent1 = p1
        self.parent2 = p2

inputs = []
while True:
    ipt = input()
    if ipt == "#":
        break
    else:
        inputs.append(ipt)