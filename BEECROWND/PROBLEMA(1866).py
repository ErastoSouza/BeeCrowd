from sys import stdin

n = int(stdin.readline())

for i in range(n):
    entrada = int(stdin.readline())
    if entrada%2 == 0:
        print(0)
    else:
        print(1)