from sys import stdin

x = int(stdin.readline())
y = int(stdin.readline())

if x > y:
    m = x
    n = y
else:
    m = y
    n = x
for i in range(n, m):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
    