#!/usr/bin/python
#coding: utf-8
import time
from math import sqrt
import getpass
#Декоратор, показывающий время работы функции
def timer(func):
    def tmp(*args, **kwargs):
        time_zero=time.time()
        print 'Время работы функции: {}'.format((time.time()-time_zero))
        print 'Результат работы функции: {}'.format(func(*args,**kwargs))
    return tmp
#Декоратор, выводящий имя функции перед результатом ее работы
def name_of_func(func):
    def tmp(*args,**kwargs):
        print 'Имя функции: {}'.format(func.__name__)
        print 'Результат работы функции: {}'.format(func(*args,**kwargs))
    return tmp
#Декоратор, запрещающий выполнение функции, если скрипт запущен
#не от указанного пользователя.
def user(func):
    login=getpass.getuser()
    def tmp(*args, **kwargs):
        if login!='admin':
            return 'Вам запрещено выполнение этой функции'
        else:
            return 'Результат работы функции: {}'.format(func(*args,**kwargs))
    return tmp
#Декоратор. Если функция вернула True, не делает ничего, если
#вернула строку, выбрасывает исключение, с этой строкой в
#качестве параметра.
class Exception(Exception): pass
def exception(func):
    def tmp(*args,**kwargs):
        result=func(*args,**kwargs)
        if result is not True:
            try:
                if type(result)==str:
                    raise Exception(result)
            except Exception, result:
                print 'Функция вернуля строку: "{}"'.format(result)
        else:
            print func(*args,**kwargs)
    return tmp



print '!!!!timer'
@timer
def multipliers(n):
 a=int(sqrt(n))
 multipliers_of_n=[]
 for i in range (1, a):
     if (n%i)==0:
         multipliers_of_n.append(i)
         n=(n//i)
 return multipliers_of_n
print multipliers(30030)


print '!!!!Имя функции'
@name_of_func
def letters(string):
 up_string=string.upper()
 up_letter=[]
 for i in range (len(string)):
     if up_string[i]==string[i] and string[i]!=' ':
         up_letter.append(string[i])
 return up_letter
print letters("Trees Are So Kind")


print '!!!!Имя пользователя'
@user
def simple(a):
 counter=0
 for i in range(1, a):
     if a%i==0:
         counter+=1
 if counter>1:
     return a, 'isnt simple'
 else:
     return a,'is simple'
 return multipliers_of_n
print simple(287)


print '!!!!true'
@exception
def summ(num1, num2):
 sum=num1+num2
 return sum
print summ (25, 35)