#!/usr/bin/python
#coding: utf-8


 #x1=a-a*b=a(1-b)
 #x2=a+a*b=a(1+b)

def ggg(list_1, list_2):
    x1=[item*(1-elem) for item in list_1 for elem in list_2]
    x2=[item*(1+elem) for item in list_1 for elem in list_2]
    return x1,x2
print ggg([100,200,300], [0.1,0.2,0.3])
    
    #if len(list_1[:item])==len(list_2[:elem])
    
    
    
    
    
