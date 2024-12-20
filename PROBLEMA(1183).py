import math

matriz = [[0.0 for _ in range(12)] for _ in range(12)]
op = input()
s=0
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
        if j>i:
            s += matriz[i][j]

if op == 'S':
    print(f"{s:.1f}")
else:
    print(f"{math.ceil(s/12):.1f}")