# Fibonacci

def fibo(x):
    fib = [1]
    n = 0
    seq = 1

    while n < x:
        fib.append(seq)
        seq = seq + fib[-2]
        n += 1
    return fib


x = int(input("Quantos números você quer na sequência de Fibonacci? "))

print(fibo(x))


