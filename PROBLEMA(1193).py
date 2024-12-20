loop = int(input())

for i in range (loop):
    entrada = input().split()
    print(f"Case {i+1}:")
    if entrada[1] == 'bin':
        dec = int(entrada[0], 2)
        hexa = hex(dec)
        for j in range(2):
            hexa = hexa.replace(hexa[0], "",1)
        print(f"{dec} dec")
        print(f"{hexa} hex")
        print()
    elif entrada[1] == 'dec':
        bina = bin(int(entrada[0]))
        hexa = hex(int(entrada[0]))
        for j in range(2):
            hexa = hexa.replace(hexa[0], "",1)
            bina = bina.replace(bina[0], "",1)
        print(f"{hexa} hex")
        print(f"{bina} bin")
        print()
    else:
        dec = int(entrada[0], 16)
        bina = bin(dec)
        for j in range(2): 
            bina = bina.replace(bina[0], "",1)
        print(f"{dec} dec")
        print(f"{bina} bin")
        print()