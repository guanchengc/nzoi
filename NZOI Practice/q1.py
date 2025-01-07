answer = input().replace(" ", "")
place1, place2, try1, try2 = input().split()
if answer[int(place1) - 1] == try1 and answer[int(place2) - 1] == try2:
    print("correct")
else:
    print("error")