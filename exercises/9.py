import random
import os

i = random.randint(1, 9)


while True:
    n = input('Adivinhe um número de 1 a 9: ')
    os.system('clear')
    
    if n.isdigit():
        if int(n) == i:
            print('Você acertou! 👏')
            print()
            i = random.randint(1, 9)
        else:
            print('Errou! 🚫 Tente novamente.')
            print()
    elif n.lower() == 'sair':
        break
    else:
        print('Ooops, algo deu errado. 🤷')
        print()
        