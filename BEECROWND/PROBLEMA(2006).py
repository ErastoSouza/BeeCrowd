certo = int(input())

tentativa = list(map(int, input().split()))

acertos = 0
for i in tentativa:
    if(i == certo):
        acertos += 1

print(acertos)