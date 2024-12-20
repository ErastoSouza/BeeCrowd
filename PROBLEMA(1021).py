entrada = float(input())
entrada = entrada *100
cem, cinquenta, vinte, dez, cinco, dois, um, mcin, mvintec, mdez, mcinco, mum = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
while entrada >= 10000:
    cem += 1
    entrada -=10000
while entrada >= 5000:
    cinquenta += 1
    entrada -=5000
while entrada >= 2000:
    vinte += 1
    entrada -=2000
while entrada >= 1000:
    dez += 1
    entrada -=1000
while entrada >= 500:
    cinco += 1
    entrada -=500
while entrada >= 200:
    dois += 1
    entrada -=200
while entrada >= 100:
    um += 1
    entrada -=100
while entrada >= 50:
    mcin += 1
    entrada -=50
while entrada >= 25:
    mvintec += 1
    entrada -=25
while entrada >= 10:
    mdez += 1
    entrada -=10
while entrada >= 5:
    mcinco += 1
    entrada -=5
while entrada >= 1:
    mum += 1
    entrada -=1

    print("NOTAS:")
    print(f"{cem} nota(s) de R$ 100.00")
    print(f"{cinquenta} nota(s) de R$ 50.00")
    print(f"{vinte} nota(s) de R$ 20.00")
    print(f"{dez} nota(s) de R$ 10.00")
    print(f"{cinco} nota(s) de R$ 5.00")
    print(f"{dois} nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{um} moeda(s) de R$ 1.00")
    print(f"{mcin} moeda(s) de R$ 0.50")
    print(f"{mvintec} moeda(s) de R$ 0.25")
    print(f"{mdez} moeda(s) de R$ 0.10")
    print(f"{mcinco} moeda(s) de R$ 0.05")
    print(f"{mum} moeda(s) de R$ 0.01")
