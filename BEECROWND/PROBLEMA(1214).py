rep = int(input())

for j in range(rep):
    entrada= list(map(int, input().split()))
    total = 0
    for i in range(entrada[0]):
        total += entrada[i+1]
    media = total/entrada[0]
    acima = 0
    for i in range(entrada[0]):
        if entrada[i+1] > media:
            acima +=1
    x = acima*100/entrada[0]
    x = round(x, 2)
    x = f"{x:.3f}"
    print(f"{x}%")