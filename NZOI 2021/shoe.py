shoe = input()

def findShoe(shoe):
    if shoe.count("R") == 2:
        print("Dorothy is in the classroom.")
    elif shoe.count("R") == 1:
        print("Hop along Dorothy and find that other shoe.")
    else:
        print("Maybe Dorothy is in Kansas.")

findShoe(shoe)