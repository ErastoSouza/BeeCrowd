from math import sqrt
qtd = int(input())

for i in range(qtd):
    primo = True
    veri = int(input())
    if(veri <= 1):
        primo = False
    for j in range(3, int(sqrt(veri)), 2):
        if veri % j == 0:
            primo = False
            break
    if primo == True:
        print("Prime")
    else:
        print("Not Prime")