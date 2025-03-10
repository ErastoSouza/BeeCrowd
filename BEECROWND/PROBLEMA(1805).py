entrada = list(map(int, input().split()))

dif = entrada[1] - entrada[0]
soma = entrada[0] + entrada[1]
resto = int(dif/2)

total = int(dif/2 * soma)
if dif%2 == 0:
    total += entrada[0] + resto
print(total) 