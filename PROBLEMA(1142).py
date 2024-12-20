from sys import stdin

entrada = int(stdin.readline())

cont= 1
for i in range(entrada):
    while cont%4 != 0:
        print(cont, end=" ")
        cont+=1
    print("PUM")
    cont+=1