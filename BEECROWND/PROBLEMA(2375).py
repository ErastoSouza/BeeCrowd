from sys import stdin

d = int(stdin.readline())

entrada = list(map(int, stdin.readline().split()))
s = "S"
for i in entrada:
    if d> i:
        s = "N"
        break

print(s)