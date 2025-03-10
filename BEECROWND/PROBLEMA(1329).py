while True:
    n = int(input())
    if n == 0:
        break
    else:
        m, j = 0, 0
        l = list(map(int, input().split()))
        for k in l:
            if k == 0:
                m+=1
            else:
                j+=1
        print(f"Mary won {m} times and John won {j} times")
