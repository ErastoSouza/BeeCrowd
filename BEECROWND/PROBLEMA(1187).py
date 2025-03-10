op = input()
s=0

for i in range(144):
    n = float(input())
    if (i >= 1 and i<11) or (i >= 14 and i<22) or (i >= 27 and i<33) or (i >= 40 and i<44) or (i >= 53 and i<55):
        s+=n

if op == 'S':
    print(f"{s:.1f}")
else:
    print(f"{s/30:.1f}")