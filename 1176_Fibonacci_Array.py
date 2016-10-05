'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
table = []
table.append(0)
a,b = 0,1
for _ in range (10000):
    table.append(b)
    a,b = b,a+b 
    
T = int(input())
for _ in range(T):
    n = int(input())
    print('Fib(%d) = %d' %(n,table[n]))
    