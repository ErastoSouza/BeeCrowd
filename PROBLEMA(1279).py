espaco = False
while True:
    try:
        entrada = int(input())
        if espaco == False:
            espaco = True
        else:
            print()
        bi = False
        hu = False
        bu = False
        if entrada % 400 == 0:
            bi = True
        elif(entrada % 4 == 0 and entrada % 100 != 0):
            bi = True
        if entrada % 15 == 0:
            hu = True
        if entrada % 55 == 0 and bi == True:
            bu = True
        if bi == True:
            print("This is leap year.")
        if hu == True:
            print("This is huluculu festival year.")
        if bu == True:
            print("This is bulukulu festival year.")
        if bi == False and hu == False:
            print("This is an ordinary year.")
    except EOFError:
        break
    