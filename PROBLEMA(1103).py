while True:
    entrada = list(map(int, input().split()))
    h1,m1,h2,m2 = entrada[0], entrada[1], entrada[2], entrada[3]
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    else:
        parada = h2*60+m2
        comeco = h1*60+m1
        cont = 0
        while comeco != parada:
            cont+=1
            comeco +=1
            if comeco == 24*60:
                comeco = 0
        print(cont)