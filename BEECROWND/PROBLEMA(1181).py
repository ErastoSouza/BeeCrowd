from sys import stdin
import math
n = int(stdin.readline())
l = stdin.readline()
s = 0
for i in range(144):
    entrada = float(input())
    if i>=n*12 and i<n*12+11:
        s+= entrada
if l == 'S':
    print(f"{s:.1f}")
else:
    print(f"{math.ceil(s/12):.1f}")