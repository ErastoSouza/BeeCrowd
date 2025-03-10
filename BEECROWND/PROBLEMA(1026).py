while True:
    try:
        entrada = list(map(int, input().split()))
        resultado = entrada[0]^entrada[1]
        print(resultado)
    except EOFError:
        break