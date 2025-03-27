# List overlap

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersecao = []

inter_s_duplicada = []

for x in a:
    if x in b:
        intersecao.append(x)
    else:
        continue

for val in intersecao:
    if val not in inter_s_duplicada:
        inter_s_duplicada.append(val)
    

print(inter_s_duplicada)