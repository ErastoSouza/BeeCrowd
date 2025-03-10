while True:
    try:
        n = int(input())
        l = list(map(int, input().split()))
        v = -1
        for i in l:
            if i>v:
                v = i
        if v <10:
            print(1)
        elif v>=20:
            print(3)
        else:
            print(2)

    except EOFError:
        break