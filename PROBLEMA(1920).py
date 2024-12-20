from sys import stdin

reguas = list(map(int, stdin.readline().split()))

tomadas = 0
for i in range(4):
    if i != 3:
        tomadas += reguas[i] - 1
    else:
        tomadas += reguas[i]

print(tomadas)