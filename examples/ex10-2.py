def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def print_fibo(k):
    p = 1
    while p <= k:
        print(p,fibo(p))
        p = p+1

print_fibo(10)

