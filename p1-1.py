#!/usr/bin/python
from math import sqrt
def multipliers(n): #1.a
 a=int(sqrt(n))
 multipliers_of_n=[]
 for i in range (1, a):
     if (n%i)==0:
         multipliers_of_n.append(i)
         n=(n//i)
 return multipliers_of_n
def equation(a,b,c): #1.b
 #ax^2+bx+c=0
 if b**2-4*a*c<0:
     return 'deistvitelnyh korney net'
 else:
     return round((-b+sqrt(b**2-4*a*c))/2*a, 2), round((-b-sqrt(b**2-4*a*c))/2*a, 2)
def simple(a): #1.c
 counter=0
 for i in range(1, a):
     if a%i==0:
         counter+=1
 if counter>1:
     return a, 'isnt simple'
 else:
     return a,'is simple'
def atm(summ): #1.d
 b=0
 i=0
 q=''
 for nominal in 100, 50, 20, 10, 5, 1:
     b=summ//nominal
     summ=summ-(summ//nominal)*nominal
     i+=b
     print b, 'banknot po',nominal, 'deneg'
 return 'vsego', i, 'banknot'
print multipliers(30030)
print equation(2, 19, 35)
print simple(13)
print atm(287)
