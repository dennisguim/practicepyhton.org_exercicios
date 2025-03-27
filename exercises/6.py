# String list Palíndromo

a = input('frase 1: ')
b = ""

a1 = ''
b1 = ''
"""b2 = ''"""
n = -1

for i in a:
   b += a[n] 
   n -= 1


for i in a:
    if i == ' ':
        i = ''
        a1 += i
    else:
        a1 += i

for i in b:
    if i == ' ':
        i = ''
        b1 += i
    else:
        b1 += i

"""for i in b1:
   b2 += b1[n] 
   n -= 1"""

pal =  'é palíndromo' if a1.lower() == b1.lower() else "não é palíndromo"


print(a1)
print(b1)
print(pal)
