# Password Generator 
import random

simbolos = ['.', '_', '!', '@', '-']
alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
palavra_chave = 'dennis'

senha = ''

for i in palavra_chave:
    set(simbolos)
    set(alfabeto)
    n = random.randint(0, 25)
    m = random.randint(0, 4)
    a = set()
    a.add(simbolos[m])
    a.add(alfabeto[n])
    a.add(i)
    for x in a:
        senha += x

print(senha)


