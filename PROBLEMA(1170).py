qtd = int(input())
dias = 0

for i in range(qtd):
    comida = float(input())
    while comida > 1:
        comida /= 2
        dias += 1
    print(f"{dias} dias")
    dias = 0