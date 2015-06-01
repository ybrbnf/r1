#!/usr/bin/python
#coding: utf-8
#x1=a-a*b=a(1-b)
#x2=a+a*b=a(1+b)
#if len(list_1[:item])==len(list_2[:elem])
def func(list_1, list_2):
 step=max(len(list_1),len(list_2))
 list_out=[]
 count=0
 interval=tuple()
 lower_bound=[item*(1-elem) for item in list_1 for elem in list_2]
 upper_bound=[item*(1+elem) for item in list_1 for elem in list_2]
 for index_1 in range(len(lower_bound)):
    for index_2 in range(len(upper_bound)):
        if index_1==index_2==count:
            count+=step
            interval=(lower_bound[index_1],upper_bound[index_2])
            list_out.append(interval)
 return list_out
print func([100,200,300], [0.1,0.2,0.3])