from sys import stdin

n = int(stdin.readline())

for i in range(n):
    entrada = list(map(int, stdin.readline().split()))

    x, y = entrada[0], entrada[1]
    r = 9*x**2+y**2
    b = 2*x**2+25*y**2
    c = -100*x+y**3

    if r > b and r > c:
        print("Rafael ganhou")

    elif b > r and b > c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
