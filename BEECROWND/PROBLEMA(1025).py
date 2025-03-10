def busca_binaria(vetor, valor):
  
  inicio = 0
  fim = len(vetor) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2  

    if vetor[meio] == valor:
      return meio  
    elif valor < vetor[meio]:
      fim = meio - 1  
    else:
      inicio = meio + 1  

  return -1 

cont = 0
while True:
    entrada = list(map(int, input().split()))
    if entrada[0] == 0:
        break
    else:
        lista = []
        for i in range(entrada[0]):
            m = int(input())
            lista.append(m)
        lista.sort()
        print(f"CASE# {cont+1}:")
        for j in range(entrada[1]):
            n = int(input())
            resultado = busca_binaria(lista, n)
            if resultado == 0:
                   print(f"{n} found at {resultado+1}")
            elif resultado != -1:
                while lista[resultado] == n and resultado != 0:
                   resultado -=1
                print(f"{n} found at {resultado+2}")
            else:
                print(f"{n} not found")
            
        cont+=1