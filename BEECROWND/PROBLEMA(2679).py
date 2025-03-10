from sys import stdin

entrada = int(stdin.readline())

if entrada % 2 == 0:
    print(entrada+2)
else:
    print(entrada+1)