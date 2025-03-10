from sys import stdin

while True:
    mesmo = list(map(int, stdin.readline().split()))
    a, b = mesmo[0], mesmo[1]
    if a == 0 and b == 0:
        break
    else:
        ana = list(map(int, stdin.readline().split()))
        bea = list(map(int, stdin.readline().split()))
        if a > b:
            m = a
            n = b
            aux = ana
            ana = bea
            bea = aux
        else:
            m = b
            n = a
        i, j, qtd = 0, 0, n
        for i in range(n):
            if i != n-1:
                if ana[i+1] == ana[i]:
                    qtd -=1
                else:
                    while bea[j] <= ana[i]:
                        if bea [j] == ana[i]:
                            qtd -= 1
                            break
                        j+=1
            else:
                while bea[j] <= ana[i]:
                        if bea [j] == ana[i]:
                            qtd -=1
                            break
                        j+=1
    print(qtd)

