# Cows And Bulls

import random

numero_random = str(random.randint(1000, 9999))
numero_acertado = '____'
n = 0
acertos = ""
print(numero_random)

""" for l in numero_acertado:
    jogador_list.append(l)
 """



while True:
    numero_jogador = input('Tente um número de 4 dígitos: ')
    for numero in numero_jogador:
        if numero_jogador[n] == numero_random[n]:
            print('cow')
            n += 1
        if numero in numero_random:
            print('bull')
    
           