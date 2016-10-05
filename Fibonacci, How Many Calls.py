def fib(n):
    f = [0] * (n+1)
    cl = [0] * (n+1)
    f[1] = 1
    cl[1] = 0
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
        cl[i] = cl[i-1] + cl[i-2] + 2
    return cl[n], f[n]

T = int(input())
for _ in range(T):
    n = int(input())
    c,r = fib(n)
    print("fib(%d) = %d calls = %d" %(n,c,r))