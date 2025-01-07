def count():
    socks = []
    for x in range(7):
        socks.append(input())

    if socks.count("Red") % 2 != 0:
        return "Red"
    if socks.count("Blue") % 2 != 0:
        return "Blue"
    if socks.count("Pink") % 2 != 0:
        return "Pink"
    if socks.count("Purple") % 2 != 0:
        return "Purple"

print(count())