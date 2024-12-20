while True:
    entrada = list(map(int, input().split()))
    n,m = entrada[0], entrada[1]

    if n <= 0 or  m <= 0:
        break
    else:
        soma = 0
        if m < n:
            aux = m
            m = n
            n = aux
        for i in range(n, m+1):
            print(i, end=" ")
            soma += i
            if i == m:
                print(f"Sum={soma}")