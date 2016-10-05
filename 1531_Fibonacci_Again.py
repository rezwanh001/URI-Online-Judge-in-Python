'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
'''
table = []
a,b = 0,1
table.append(0)
for _ in range(109 + 1):
    table.append(b)
    a,b = b,a+b
'''
def Fib(n):
    a,b = 0,1
    while b<n:
        yield a 
        a,b = b, a+b 

#print(table)
#Fib(10000000)
#for i in range(len(table)):
   # print(table[i])
table = list(Fib(10000))
while True:
    try:
        n,m = map(int,input().split())
        
        #Fib(n)
    except EOFError:
        break
    print(table[(table[n])]%m)
            