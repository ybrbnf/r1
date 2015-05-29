#!/usr/bin/python
#coding: utf-8

#Функция, возвращающая несколько значений
def func_num(elem1, elem2):
    return elem1+elem2, elem1-elem2

#генератор таблицы кубов.
def func_gen_cubs():
    list=range(10)
    for elem in list:
        yield elem**3

#вложенная lambda функция.
def func_lambda(elem1, elem2):
    result=lambda elem1, elem2: elem1+elem2
    return result(elem1,elem2)

#замыкание
def func_lambda_closure(elem1):
    result=lambda elem2: elem1+elem2
    return result

#*args
def func_args(*args):
    summ=0
    for number, elem in enumerate(args):
        summ+=elem
    return summ

#**kwargs
def func_kwargs(**kwargs):
    summ=0
    for key, value in kwargs.items():
        summ+=value
    return summ


#optional и named
def func_optional_named(elem1, elem2=2, elem3=10):
    summ=elem1+elem2+elem3
    return summ 


print '!!!!функция, возвращающая несколько значений'
item1,item2=100,500
print item1, item2


print '!!!!генератор таблицы кубов'
gen_of_cubs=func_gen_cubs()
for elem in gen_of_cubs:
    print(elem)

print '!!!!вложенная lambda функция'
print func_lambda(1, 2)

print '!!!!замыкание'
summ=func_lambda_closure(1)
print summ(2)

print '!!!!*args'
print func_args(1,2,3,4,5)

print '!!!!**kwargs'
print func_kwargs(elem1=1, elem2=2, elem3=3, elem4=4, elem5=5)

print '!!!!optional & named'
print func_optional_named(3,elem3=2)