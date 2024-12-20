def fatorial(num):
    for i in range(num+1):
        if i == 0:
            resultado = 1
        else:
            resultado *= i
    return resultado

while True:
    try:
        valores = list(map(int, input().split()))
        resultado = fatorial(valores[0])+fatorial(valores[1])
        print(f"{resultado}")
    except EOFError:
        break