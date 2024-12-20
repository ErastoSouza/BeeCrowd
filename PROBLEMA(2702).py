from sys import stdin

comidas = list(map(int, stdin.readline().split()))
pessoas = list(map(int, stdin.readline().split()))

r = 0
if comidas[0] < pessoas[0]:
    r+= pessoas[0]-comidas[0]

if comidas[1] < pessoas[1]:
    r+= pessoas[1]-comidas[1]

if comidas[2] < pessoas[2]:
    r+= pessoas[2]-comidas[2]

print(r)