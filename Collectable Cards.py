def gcd(a,b):
    x,y = 0,1
    lx,ly = 1,0
    while b:
        q = a//b
        a,b = b,a%b
        x,lx = lx - q*x, x
        y,ly = ly - q*y, y

    return a

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    print(gcd(a,b))
