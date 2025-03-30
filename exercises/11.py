# Check Primality Functions 

def primo(x):
    nums = [2, 3, 5, 7]
    check = []

    for i in nums:
        p = x % i
        check.append(p)
    
    if x == 2 or x == 3 or x == 5 or x == 7:
        return f'{x} é um número primo.'
    else:
        if 0 in check:
            return f'\n{x} não é um número primo. \n'
        else:
            return f'\n{x} é um número primo. \n'

x = input("Digite um número para checar se ele é primo ou não: ")
x_1 = ""
for y in x:
   if y.isdigit():
       x_1 += y
    
       

print(primo(int(x_1)))