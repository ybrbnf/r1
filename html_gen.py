#!/usr/bin/python
#coding: utf-8
class Tree:
    def __init__(self, data=None, parent=None, space=None):
        self.data=data
        self.parent=parent
        self.space=space

    def __str__(self):
        return str(self.tag1)

in_file='in.txt'#исходный файл
out_file='out.html'#конечный файл
open_tags=[]#список открывающах тегов
close_tags=[]#список закравающ тегов
tmp=[] #временный список
counter=0
with open(in_file, 'r') as read_file:# пишем теги из файла в списки 
    for line in read_file:
        open_tags.append(line.strip('\n'))
        tmp.append('/'+line.strip('\n'))
close_tags=tmp[::-1]
for element in open_tags:
    if counter==0:
        space=0
        root=Tree(line,None,space)
        counter+=1
        print '<'+str(element)+'>'
    elif counter!=0:
        space=counter
        node=Tree(line,root,space)
        counter+=1
        print ' '*space+'<'+str(element)+'>'
counter=0
for element in close_tags:
    if counter==0:
        root=Tree(line,None,space)
        counter+=1
        print ' '*space+'<'+str(element)+'>'
    elif counter!=0:
        space=space-counter
        node=Tree(line,root,space)
        counter+=1
        print ' '*space+'<'+str(element)+'>'