n = int(input())

par = []
impar = []
for i in range(n):
    m = int(input())
    if(m%2==0):
        par.append(m)
    else:
        impar.append(m)
par.sort()
impar.sort(reverse=True)

for i in par:
    print(i)
for j in impar:
    print(j)