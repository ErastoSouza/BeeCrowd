entrada = list(map(int, input().split()))
n,m = entrada[0], entrada[1]
d = int(n/m)
r = n%m

print(f"{d} {m}")