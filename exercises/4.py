# Divisors

n = int(input('Digite um número: '))

list_divisors = []

for d in range(1, n + 1):
    if n % d == 0:
        list_divisors.append(d)
    else:
        continue

print(f"Estes são os divisores de {n}: {list_divisors}.")