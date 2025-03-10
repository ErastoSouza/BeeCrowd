from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    else:
        fila = deque()
        saida = list()
        c = True

        for i in range(1, n+1):
            fila.append(i)
        while len(fila)>1:
            if c:
                saida.append(fila.popleft())
                c = False
            else:
                fila.append(fila.popleft())
                c = True
        print("Discarded cards:", end =' ')
        for i in range(len(saida)):
            if i == len(saida)-1:
                print(saida[i])
            else:
                print(f"{saida[i]},", end=' ')
        print(f"Remaining card: {fila[0]}")