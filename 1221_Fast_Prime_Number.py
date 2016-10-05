'''
Created on Aug 9, 2016

@author: Md. Rezwanul Haque
'''
import math
def is_prime(n):
    if n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3,int(math.sqrt(n))+1, 2))
T = int(input())
for _ in range(T):
    a = int(input())
    if (is_prime(a)):
        print('Prime')
    else:
        print('Not Prime')