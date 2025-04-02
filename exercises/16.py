# Password Generator 
import random

simbolos = ['.', '_', '!', '@', '-']
alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
palavra_chave = 'dennis'
recuperar_chave = ''
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

for letra in senha:
    if letra in palavra_chave:
        recuperar_chave += letra

print(recuperar_chave)

