#Elementos da sequencia de Fibonacci
def fibo(n):
    fib = [0,1]
    if n==1:
        fib = [fib[0]]
        return fib
    elif n==2:
        return fib
    else:
        for i in range(2,n):
            fib.append((fib[i-1])+(fib[i-2]))
        return fib

n = int(input("Digite o elemento de fibonacci que você quer descobrir: "))
print(fibo(n))