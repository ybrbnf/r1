#!/usr/bin/python
#coding: utf-8
def func_list_to_dict(list1,list2):	
 print '-----------------1-4-2a----------'
 dict_out=dict(zip(list1,list2))
 return dict_out
def func_tuple_to_dict(tuple):
 print '-----------------1-4-2b----------'
 dict_out=dict(tuple)
 return dict_out
def func_find_string(dict_in, str):
 print '-----------------1-4-3----------'
 for key, value in dict_in.iteritems():
    if value==str:
        dict_in[key]=None
 return dict_in
def func_union_dict(dict_in_1, dict_in_2):
 print '-----------------1-4-4----------'
 list_x=[]
 for key in dict_in_1.iteritems():
    if key in dict_in_2:
        list_x.append(key)
 for i in list_x:
    del dict_in_1[i]
    del dict_in_2[i]
    dict_in_1.update(dict_in_2)
 return dict_in_1
def func_calc(operation,num1,num2):
 print '-----------------1-4-5----------'
 dict_out={
     '+':num1+num2,
     '-':num1-num2,
     '*':num1*num2,
     '/':num1/num2,# проверкy деления на ноль без if сделать не могу.
     } 
 print '{}{}{}={}'.format(num1,operation,num2,dict_out[operation])
def func_dict_reverce(dict_in):
 print '-----------------1-4-6----------'
 dict_out=dict((key,value) for value,key in dict_in.iteritems())   
 return dict_out
print func_list_to_dict(['a','b','c','d','e','f'],['0','1','2','3','4','5'])
print func_tuple_to_dict([('0','a'),('1','b'),('2','c')])
print func_find_string({0:'alfa',1:'beta',2:'gamma'},'beta')
print func_union_dict({0:'a',1:'b',2:'c',3:'d'},{2:'c',3:'d',4:'e',5:'f'})
print func_calc('/',40,20)
print func_dict_reverce({0:'a',1:'b',2:'c'})
