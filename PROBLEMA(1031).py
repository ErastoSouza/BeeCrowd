from collections import deque
while True:
    entrada = int(input())
    if entrada == 0: 
        break
    else:
        m = 0
        
        while True:
            m += 1
            lista = deque()
            for i in range(2,entrada+1):
                lista.append(i)
            for i in range(entrada-2):
                lista.rotate(1 - m)
                lista.popleft()
            if lista[0]==13:
                break
        print(m)