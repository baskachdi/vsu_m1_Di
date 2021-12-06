def fib(n: int):
    if n != int(n):
        return("EROR: n not integer")
    k = [0]
    if n == 1:
        return k
    elif n >= 2:
        k.append(1)
    for i in range(n-2):
        k.append(k[i]+k[i+1])
    return(k)

#print(fib(n=15))