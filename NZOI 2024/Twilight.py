def spell(u, v, maxi, a, b, c, d, current = 1):
    if current == maxi:
        return [a*u+b*v, c*u+d*v]
    else:
        return spell(a*u+b*v, c*u+d*v, maxi, a, b, c, d, current + 1)


def main():
    a, b, c, d = map(int, input().split())
    maxi = int(input())
    print(*spell(1, 1, maxi, a, b, c, d))

def test():
    print(spell(1, 1, 1000000000, 1, 1, 1, 1))

if __name__ == "__main__":
    test()