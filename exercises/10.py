import random

a = []
b = []
c = []

stop1 = 0
stop2 = 0


while stop1 != 1:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    if x > y:
        continue
    else:
        stop1 += 1

r = range(x, y)
for i in r:
    a.append(i)

while stop2 != 1:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    if x > y:
        continue
    else:
        stop2 += 1
        
r = range(x, y)
for i in r:
    b.append(i)

for i in a:
    if i in b:
        c.append(i)
 
c == c if c is not [] else ''

print(f'a = {a}' '\n')
print(f'b = {b}' '\n')

if c != '' :
    print(f'O(s) elemento(s) em comum é: {c}')
else:
    print('Não há elementos em comum')

print()


