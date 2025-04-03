# Cows And Bulls

import random

numero_random = str(random.randint(1000, 9999))
randomico = []

tent_in = []

acertados = []

for i in numero_random:
    randomico.append(i)
print(randomico)

while True:
    n = 0 #resolver, o n ta passando de 3; tem q fazer ele zerar no loop
    tentativa_input = input('tente: ')
    for i in tentativa_input:
        tent_in.append(i)
    print(tent_in)
    
    for i in tent_in:
        if i == randomico[n]:
            print('cow')
            acertados.append(i)
            n += 1
        else:
            acertados.append("-")
            n += 1
    
    print(f'n = {n}')
    print(f'acertados: {acertados}')
    