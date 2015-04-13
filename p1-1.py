#!/usr/bin/python
def multipliers(n): #1.a
 spisok=''
 b=n
 while n>=2:
  for i in range(2,n):                 
         if n%i==0:
             break                            
  else:                                    
     while b%n==0:
         spisok=spisok+str(n)+' '
         b=b/n
  n=n-1    
 return spisok
def equation(a,b,c): #1.b
 from math import sqrt
 D=0
 i=1
 D=b**2-4*a*c
 if D<0:
     return 'deistvitelnyh korney net'
 else:
     return 'korni=',round((-b+sqrt(D))/2*a, 2),';', round((-b-sqrt(D))/2*a, 2)
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
