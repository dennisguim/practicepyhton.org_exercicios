import random

a = []
b = []
c = []

x = random.randint(1, 100)
y = random.randint(1, 100)
r = 0

while True:
    if x < y:
        r = range(x, y)
        continue
    else:
        break

if x < y:
    for i in r:
        a.append(i)

x = random.randint(1, 100)
y = random.randint(1, 100)
if x < y:
    for i in r:
        b.append(i)

for i in a:
    if i in b:
        c.append(i)
    else:
        c = ''

print(f'a = {a}' '\n')
print(f'b = {b}' '\n')

if c != '' :
    print(f'O(s) elemento(s) em comum é: {c}')
else:
    print('Não há elementos em comum')

print()


