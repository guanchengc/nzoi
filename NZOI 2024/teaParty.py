ipt = list(map(int, input().split()))
guest = ipt[0]
host = ipt[1]
favors = []
counts = [0, 0, 0, 0, 0, 0]
for x in range(guest):
    inpt = input()
    favors.append(inpt.split()[1])
    if inpt.split()[1] == "G":
        counts[0] += 1
    if inpt.split()[1] == "C":
        counts[1] += 1
    if inpt.split()[1] == "E":
        counts[2] += 1
    if inpt.split()[1] == "P":
        counts[3] += 1
    if inpt.split()[1] == "L":
        counts[4] += 1
    if inpt.split()[1] == "S":
        counts[5] += 1

storage = {}
for x in range(guest):
    ipt = input().split()
    storage[ipt[0]] = ipt[1:]

possibleHosts = []
for x in range(host):
    possibleHosts.append(input())

for hosts in possibleHosts:
    conditionsNotMet = 0
    
            
    if counts[0] > int(storage[hosts][0]):
        conditionsNotMet += counts[0] - int(storage[hosts][0])
    if counts[1] > int(storage[hosts][1]):
        conditionsNotMet += counts[1] - int(storage[hosts][1])
    if counts[2] > int(storage[hosts][2]):
        conditionsNotMet += counts[2] - int(storage[hosts][2])
    if counts[3] > int(storage[hosts][3]):
        conditionsNotMet += counts[3] - int(storage[hosts][3])
    if counts[4] > int(storage[hosts][4]):
        conditionsNotMet += counts[4] - int(storage[hosts][4])
    if counts[5] > int(storage[hosts][5]):
        conditionsNotMet += counts[5] - int(storage[hosts][5])

    if conditionsNotMet > 0:
        if conditionsNotMet <= 2:
            print(hosts + " Mildly Successful (" + str(conditionsNotMet) + ")")
        else:
            print(hosts + " Disaster (" + str(conditionsNotMet) + ")")
    else:
        print(hosts + " Successful")