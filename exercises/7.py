# List comprehesion - list only even

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

par = []

for n in a:
    if n % 2 == 0:
        par.append(n)

print(par)    