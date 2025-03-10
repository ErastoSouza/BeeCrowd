from collections import deque

def verifica(entrada):
    pilha = deque()
    q=0

    for caractere in entrada:
        if caractere == '<':
            pilha.append(caractere)
        elif caractere == '>':
            if pilha:
                pilha.pop()
                q+=1
    return q

n = int(input())
for i in range(n):
    entrada = input().strip()
    print(verifica(entrada))