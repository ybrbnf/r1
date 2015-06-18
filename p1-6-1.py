#!/usr/bin/python
#coding: utf-8

import itertools
result=[]
#Три примера list comprehensions, возвращающих итератор

def func_iter(list_1, list_2):
    list_1=[elem**2 for elem in list_1] #модификация
    list_2=[elem**2 for elem in list_2 if elem%2==0] #условие
    return [elem**2 for elem in list_1 if elem in list_2] # два списка


#Три примера list comprehensions, возвращающих генератор

#модификация
def func_gen_1(list_1,list_2):
    list_1=(elem**2 for elem in list_1)
    return list_1


#услови
def func_gen_2(list_1,list_2):
    list_2=(elem**2 for elem in list_2 if elem%2==0)
    return list_2


#два списка
def func_gen_3(list_1, list_2):
    return (elem**2 for elem in list_1 if elem in list_2)



#Пять примеров использования itertools
print 'итератор'
print func_iter([1,2,3],[2,3,4,5])
print '-------------------------------------------'

print 'генератор: модификация'
for elem in func_gen_1([1,2,3],[2,3,4,5]):
    print elem

print 'генератор: условие'
for elem in func_gen_2([1,2,3],[2,3,4,5]):
    print elem

print 'генератор: два списка'
for elem in func_gen_3([1,2,3],[2,3,4,5]):
    print elem

print '-------------------------------------------'


print 'пять примеров использования itertools:'
print '-------product---------'
def product(list_1, list_2):
    return itertools.product(list_1, list_2, repeat=1)
print '{}'.format([item for item in product('ABC', 'x')])
    
print '-------izip_longest---------'
def izip(list_1, list_2):
    return itertools.izip_longest(list_1, list_2, fillvalue='@')
print '{}'.format([item for item in izip([1,2,3,4,5], ['a','b','c'])])
    
print '-------combinations_with_replacement---------'
def combin_with_repl (iter, r):
    return itertools.combinations_with_replacement(iter, r)
print '{}'.format([item for item in combin_with_repl('ABC', 2)])
    
print '-------permutations---------'
def permutations(iter):
    return itertools.permutations(iter, r=2)
print '{}'.format([item for item in permutations('ABC')])

print '-------compress---------'    
def compres (data, key):
    return itertools.compress(data, key)
print '{}'.format([item for item in compres('fg4n6gf4gf54b6gf4b6', [0,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1])])
