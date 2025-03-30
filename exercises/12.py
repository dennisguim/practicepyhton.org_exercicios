# List Ends
# try to generate random number list with import random

import random

def nova_lista():
    n = random.randint(3, 10)
    a = random.sample(range(0, 100), n)
    b =[]
    b.append(a[0])
    b.append(a[-1])
    return a, b

lista_original, lista_gerada = nova_lista()
print(
    f'Lista original = {lista_original}',
    f'\nLista gerada = {lista_gerada}'
    )