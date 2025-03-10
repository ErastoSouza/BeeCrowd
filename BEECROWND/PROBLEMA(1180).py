n = int(input())

entrada = list(map(int, input().split()))
m = entrada[0]
p = 0

for i in range(1,n):
    if entrada[i]<m:
        m = entrada[i]
        p = i
print(f"Menor valor: {m}")
print(f"Posicao: {p}")