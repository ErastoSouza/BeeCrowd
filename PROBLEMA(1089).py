from sys import stdin
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    else:
        picos = 0
        vetor = list(map(int, stdin.readline().split()))
        for i in range(n):
            if i == 0:
                if vetor[i] > vetor[i+1] and vetor[i] > vetor[n-1]:
                    picos +=1
                elif vetor[i] < vetor[i+1] and vetor[i] < vetor[n-1]:
                    picos += 1
            elif i == n-1:
                if vetor[i] > vetor[0] and vetor[i] > vetor[i-1]:
                    picos +=1
                elif vetor[i] < vetor[0] and vetor[i] < vetor[i-1]:
                    picos += 1
            else:
                if vetor[i-1] < vetor[i] and vetor[i+1]< vetor[i]:
                    picos+=1
                elif vetor[i-1] > vetor[i] and vetor[i+1] > vetor[i]:
                    picos += 1
        print(picos)
