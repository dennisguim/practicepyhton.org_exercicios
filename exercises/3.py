#list less then
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
check = input('Which value? ')
list1 = []

for i in a:
    if int(i) <= int(check):
        list1.append(i)
    else:
        continue

print(list1)


