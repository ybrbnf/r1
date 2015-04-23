#!/usr/bin/python

from math import sqrt
def multipliers(n): #1.a
 a=int(sqrt(n))
 b=[]
 for i in range (1, a):
     if (n%i)==0:
         b.append(i)
         n=(n//i)
 return b

def equation(a,b,c): #1.b
 d=0
 i=1
 d=b**2-4*a*c
 if d<0:
     return 'deistvitelnyh korney net'
 else:
     return round((-b+sqrt(d))/2*a, 2), round((-b-sqrt(d))/2*a, 2)

def simple(a): #1.c
 x=0
 for i in range(1, a):
     if a%i==0:
         x+=1
 if x>1:
     return a, 'isnt simple'
 else:
     return a,'is simple'

def atm(c): #1.d
 b=0
 i=0
 q=''
 for a in 100, 50, 20, 10, 5, 1:
     b=c//a
     c=c-(c//a)*a
     i+=b
     print b, 'banknot po',a, 'deneg'
 return 'vsego', i, 'banknot'
print multipliers(30030)
print equation(2, 19, 35)
print simple(13)
print atm(287)
