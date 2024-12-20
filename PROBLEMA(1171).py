loop = int(input())
tudo = []
cont = 0
for i in range(loop): 
    entrada = int(input())
    tudo.append(entrada)

tudo.sort()
print(tudo)
i,j =0, 0
num = tudo[0]
while i <= len(tudo):
    if i == len(tudo):
        print(f'{num} aparece {cont} vez(es)')
        break
    if tudo[i] == num:
        cont+=1
        i+= 1
    else:
        print(f'{num} aparece {cont} vez(es)')
        num = tudo[i]
        cont = 0