from math import gcd

cont = int(input())

for i in range(cont):
    qtd = list(map(int, input().split()))
    resultado = gcd(qtd[0], qtd[1])
    print(resultado)