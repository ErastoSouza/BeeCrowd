from sys import stdin

entrada = list(map(int, stdin.readline().split()))

print(f"{entrada[0]/entrada[1]:.2f}")