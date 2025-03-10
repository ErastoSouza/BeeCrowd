from sys import stdin

entrada = list(map(int, stdin.readline().split()))
c, n = entrada[0], entrada[1]

print(c%n)