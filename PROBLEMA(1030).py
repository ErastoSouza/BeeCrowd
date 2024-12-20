from collections import deque
loop = int(input())

for k in range(loop):
    lista = deque()
    entrada = list(map(int, input().split()))
    n, m = entrada[0], entrada[1]
    for i in range(1,n+1):
        lista.append(i)
    for i in range(n-2):
        lista.rotate(-(m-1))
        lista.popleft()
    
    print(f"Case {k+1}: {lista[0]}")


