def quicksort_por_tamanho_string(lista):

  if len(lista) <= 1:
    return lista 
  
  pivo = lista[0]

  menores = [s for s in lista[1:] if len(s) >= len(pivo)]
  maiores = [s for s in lista[1:] if len(s) < len(pivo)]

  # Recursivamente ordena as sublistas e combina os resultados
  return quicksort_por_tamanho_string(menores) + [pivo] + quicksort_por_tamanho_string(maiores)
n = int(input())

for i in range(n):
    entrada = input().split()
    lista = quicksort_por_tamanho_string(entrada)
    for i in lista:
        print(i, end=" ")
    print("\t")
