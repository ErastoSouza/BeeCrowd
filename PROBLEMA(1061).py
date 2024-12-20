from sys import stdin

entrada = stdin.readline()
comeco = int(entrada[4])*86400

entrada = list(map(int, input().split(":")))

for i in range(3):
    if i ==0:
        comeco += entrada[i]*3600
    if i ==1:
        comeco += entrada[i]*60
    if i ==2:
        comeco += entrada[i]

entrada = stdin.readline()
saida = int(entrada[4])*86400

entrada = list(map(int, input().split(":")))

for i in range(3):
    if i ==0:
        saida += entrada[i]*3600
    if i ==1:
        saida += entrada[i]*60
    if i ==2:
        saida += entrada[i]

fim = saida - comeco

dia, hora, minutos = 0, 0, 0

while fim >= 86400:
    dia+=1
    fim -=86400
while fim >= 3600:
    hora+=1
    fim -= 3600
while fim >= 60:
    minutos += 1
    fim -= 60

print(dia)
print(hora)
print(minutos)
print(fim)