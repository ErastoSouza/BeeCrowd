while True:
    try:
        soldados = list(map(int, input().split()))
        saida = abs(soldados[0]-soldados[1])
        print(saida)
    except(EOFError):
        break