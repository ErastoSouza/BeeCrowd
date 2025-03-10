while True:
    entrada = list(map(int, input().split()))
    x1, y1, x2, y2 = entrada[0], entrada[1], entrada[2], entrada[3]
    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        break
    else:
        x = abs(x1-x2)
        y = abs(y1-y2)
        if x == 0 and y == 0:
            print(0)
        elif x==y or x==0 or y ==0:
            print(1)
        else:
            print(2)