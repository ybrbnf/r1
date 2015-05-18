#!/usr/bin/python
#coding: utf-8
def func_calc(operation,num1,num2):
 try:
  print '-----------------1-4-5----------'
  dict_out={
      '+':num1+num2,
      '-':num1-num2,
      '*':num1*num2,
      '/':num1/num2,
      } 
 except ZeroDivisionError:
    print 'Деление на ноль. Введите другое значение num2'
 else:
    print '{}{}{}={}'.format(num1,operation,num2,dict_out[operation])
 finally:
    return('Расчет окончен')
print func_calc('/',40,0)
    