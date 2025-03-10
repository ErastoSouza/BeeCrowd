n = int(input())
for j in range(n):
    m = int(input())
    a, b = 0, 1
    for i in range(m):
        a, b = b, a + b 
    print(f"Fib({m}) = {a}")