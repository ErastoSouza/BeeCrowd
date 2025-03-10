from sys import stdin

entrada = list(map(int, stdin.readline().split()))
maior = entrada[0]
for i in entrada:
    if i > maior:
        maior = i
print (maior)