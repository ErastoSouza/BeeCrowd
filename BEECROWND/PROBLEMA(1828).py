n = int(input())

for i in range(n):
    entrada = input().split()
    s, r = entrada[0], entrada[1]

    if(s[0] == 'p' and s[1] == 'e'):
        if (r[0] == 'l' or r[0] == 't'):
            print(f"Caso #{i+1}: Bazinga!")
        elif((r[0] == 'p' and r[1] == 'a') or r[0] == 'S'):
            print(f"Caso #{i+1}: Raj trapaceou!")
        else:
            print(f"Caso #{i+1}: De novo!")

    if(s[0] == 'p' and s[1] == 'a'):
        if ((r[0] == 'p' and r[1] == 'e') or r[0] == 'S'):
            print(f"Caso #{i+1}: Bazinga!")
        elif r[0] == 'l' or r[0] == 't':
            print(f"Caso #{i+1}: Raj trapaceou!")
        else:
            print(f"Caso #{i+1}: De novo!")
    
    if(s[0] == 't'):
        if ((r[0] == 'p' and r[1] == 'a') or r[0] == 'l'):
            print(f"Caso #{i+1}: Bazinga!")
        elif r[0] == 'p' and r[1] == 'e' or r[0] == 'S':
            print(f"Caso #{i+1}: Raj trapaceou!")
        else:
            print(f"Caso #{i+1}: De novo!")
    
    if(s[0] == 'l'):
        if ((r[0] == 'p' and r[1] == 'a') or r[0] == 'S'):
            print(f"Caso #{i+1}: Bazinga!")
        elif r[0] == 'p' and r[1] == 'e' or r[0] == 't':
            print(f"Caso #{i+1}: Raj trapaceou!")
        else:
            print(f"Caso #{i+1}: De novo!")
    
    if(s[0] == 'S'):
        if ((r[0] == 'p' and r[1] == 'e') or r[0] == 't'):
            print(f"Caso #{i+1}: Bazinga!")
        elif r[0] == 'p' and r[1] == 'a' or r[0] == 'l':
            print(f"Caso #{i+1}: Raj trapaceou!")
        else:
            print(f"Caso #{i+1}: De novo!")