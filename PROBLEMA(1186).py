
matriz = [[0.0 for _ in range(12)] for _ in range(12)]
op = input()
s=0

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

x = 1

for i in range(1, 12):
    for j in range(12-i, 12):
        s += matriz[i][j]

if op == 'S':
    print(f"{s:.1f}")
else:
    print(f"{s/66:.1f}")