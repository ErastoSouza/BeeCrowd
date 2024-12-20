from collections import deque
from sys import stdin


while True:
    pilha, c = deque(), 0
    try:
        entrada = stdin.readline().strip()
        for i in entrada:
            if i == '(':
                pilha.append(i)
            elif i ==')':
                if not pilha:
                    print("incorrect")
                    c=1
                    break
                else:
                    pilha.pop()   
        if c==0:
            print("correct")
        
    except EOFError:
        break