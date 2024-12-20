while True:
    entrada = input().split()
    if entrada[0] == '0' and entrada[1] == '0':
        break
    c = 0
    total = 0
    if len(entrada[0])>=len(entrada[1]):
        menor, menor = 1, 0
    else:
        maior,menor = 1, 0
    
    tam = len(entrada[menor])  
    dif = len(entrada[maior]) - len(entrada[menor])

    for i in range(tam -1, -1, -1):
        aux1 , aux2 = int(entrada[maior][i+dif]), int(entrada[menor][i])
        total += aux1 + aux2
        if total >=10:
            c += 1
            total = 1
        else:
            total = 0
    while dif>0:
        aux1 =int(entrada[maior][dif-1])
        total += aux1
        if total >=10:
            c += 1
            total = 1
        else:
            total = 0
        dif-=1
    
    if c == 1:
        print(f"{c} carry operation.")
    elif c == 0:
        print(f"No carry operation.")
    else:
        print(f"{c} carry operations.")
    