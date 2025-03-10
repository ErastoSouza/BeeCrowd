while True:
    entrada = input()
    if entrada [0] == '-':
        break
    elif entrada[1] == 'x':
        saida1 = int(entrada, 16)
        print(saida1)
    else:
        saida = hex(int(entrada))
        saida = saida.upper()
        saida = saida.replace('X','x',1)
        print(saida)