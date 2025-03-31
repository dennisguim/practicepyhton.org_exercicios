def fun(n):
    return lambda x: x * n

# creating mutiliplier functions 
double = fun(2)
triple = fun(3)

print(double(5))  
print(triple(5))  


