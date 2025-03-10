from sys import stdin

entrada = list(map(float, stdin.readline().split()))

soma = 0
for i in range(4):
    if i == 0:
     soma += entrada[i]*2
    if i == 1:
       soma += entrada[i]*3
    if i == 2:
       soma += entrada[i]*4
    if i == 3:
       soma += entrada[i]

nf = soma/10

if nf>=5 and nf<7:
    print(f"Media: {nf:.1f}")
    print("Aluno em exame.")
    r = float(stdin.readline())
    print(f"Nota do exame: {r:.1f}")
    nf = (nf+r)/2
    if nf >=5:
        print("Aluno aprovado.")
        print(f"Media final: {nf:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {nf:.1f}")
      
if nf<5:
   print(f"Media: {nf:.1f}")
   print("Aluno reprovado.")
if nf>7:
   print(f"Media: {nf:.1f}")
   print("Aluno aprovado.")