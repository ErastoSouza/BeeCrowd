from sys import stdin

n = int(stdin.readline())
for i in range(n):
    entrada = stdin.readline().split()
    if entrada[0] == "Thor":
        print("Y")
    else:
        print("N")