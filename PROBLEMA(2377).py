from sys import stdin

dp = list(map(int, stdin.readline().split()))
custo = list(map(int, stdin.readline().split()))

qp = int(dp[0]/dp[1])

custo = qp*custo[1]+ custo[0]*dp[0]
print(custo)
