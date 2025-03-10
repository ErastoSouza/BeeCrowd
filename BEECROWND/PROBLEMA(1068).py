from collections import deque

def verifica_parenteses(expressao):
    pilha = deque()
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False
            pilha.pop()
    return not pilha

while True:
    try:
        expressao = input().strip()
        if verifica_parenteses(expressao):
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break