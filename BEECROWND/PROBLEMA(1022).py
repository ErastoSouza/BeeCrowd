from math import gcd
v = int(input())
for i in range(v):
    entrada = input().split()

    N1 = int(entrada[0])
    D1 = int(entrada[2])
    N2 = int(entrada[4])
    D2 = int(entrada[6])
    operacao = entrada[3]

    if(operacao == '+'):
        resultado1 = (N1*D2 + N2*D1)
        resultado2 = (D1*D2)
    elif(operacao == '-'):
        resultado1 = (N1*D2 - N2*D1)
        resultado2 = (D1*D2)
    elif(operacao == '*'):
        resultado1 = (N1*N2)
        resultado2 = (D1*D2)
    else:
        resultado1 = (N1*D2)
        resultado2 = (N2*D1)
    mdc  = gcd(resultado1, resultado2)

    resultado3 =int(resultado1/mdc)
    resultado4 =int(resultado2/mdc)

    print(f"{resultado1}/{resultado2} = {resultado3}/{resultado4}")