import random

simbolos = ['.', '_', '!', '@', '-']
alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
numeros = range(0, 9)


def senha_forte(palavra):
    palavra_chave = palavra
    palavra_emb = set()
    senha = ''
    for i in palavra_chave:
        i_emb = [i.lower(), i.upper()]
        o = random.randint(0, 1)
        i = i_emb[o]
        if i != " ":
            palavra_emb.add(i_emb[o])

    for i in palavra_emb:
        set(simbolos)
        set(alfabeto)
        n = random.randint(0, 25)
        m = random.randint(0, 4)
        
        a = set()
        a.add(simbolos[m])
        a.add(alfabeto[n])
        a.add(str(random.randint(0,9)))
        a.add(i)
        for x in a:
            senha += x
    return senha

print(senha_forte(input('Digite a palavra-chave: ')))

""" for letra in senha:
    if letra in palavra_chave:
        recuperar_chave += letra

print(recuperar_chave) """

