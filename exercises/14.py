# List Remove Duplicates | returns a new list that contains all the elements of the first list minus all the duplicates.

lista_a = [1, 2, 3, 4, 5, 6, 6, 2, 2, 1, 3, 4]
lista_b = []
lista_c = []

# gerar uma lista com loop
def com_loop(): 
    for i in lista_a:
        if i not in lista_b:
            lista_b.append(i)
    return lista_b
            
                  
# gerar uma lista com set()
def com_set():
    lista_c = list(set(lista_a))
    return lista_c

print(com_loop())

print(com_set())