import math

n = int(input())

for i in range(n):
    t = 0
    entrada = list(map(float, input().split()))
    pa, pb = entrada[0], entrada[1]
    ca = entrada[2]/100
    cb = entrada[3]/100
    

    while pa <= pb and t<101:
        pa += math.floor(pa * ca)
        if cb>0:
            pb += math.floor(pb * cb)
        t+=1
    if t<101:
        print(f"{t} anos.")
    else:
        print("Mais de 1 seculo.")