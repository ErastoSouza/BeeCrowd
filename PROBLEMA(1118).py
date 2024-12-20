v = True
while v:
    while True:
        x = float(input())
        if x<=10 and x>=0:
            break
        else:
            print("nota invalida")
    while True:
        y = float(input())
        if y<=10 and y>=0:
            break
        else:
            print("nota invalida")

    media = (x+y)/2
    print(f"media = {media:.2f}")
    while True:
        print("novo calculo (1-sim 2-nao)")
        resposta = float(input())
        if resposta == 1:
            break
        elif resposta == 2:
            v = False
            break

