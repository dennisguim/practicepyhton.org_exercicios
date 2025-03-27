

current_year = 2025


contador = 0 

while True:
    name = input("What is your name? ")
    
    if name == 'sair':
        break
    else:
        age = input("How old are you? ")
        hundred = 2025 + (100 - int(age))
        contador += 1
        print(f'Round {contador}: {name}, in {hundred} you will be a hundred years old')


