#!/usr/bin/python
#coding: utf-8
class Tree:
    def __init__(self, data=None, parent=None, space=None):
        self.data=data
        self.parent=parent
        self.space=space

    def __str__(self):
        return str(self.data)

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
out_file=open('out.html', 'w')
for element in open_tags:
    if counter==0:
        space=0
        root=Tree(element,None,space)
        out_file.write (' '*space+'<{}>\n'.format(element))
        counter+=1
        
    elif counter!=0:
        space=counter
        node=Tree(element,root,space)
        out_file.write (' '*space+'<{}>\n'.format(element))
        counter+=1
counter=0
for element in close_tags:
    if counter==0:
        root=Tree(element,None,space)
        out_file.write (' '*space+'<{}>\n'.format(element))
        counter+=1
        
    elif counter!=0:
        node=Tree(element,root,space)
        out_file.write (' '*space+'<{}>\n'.format(element))
        counter+=1
        space=space-counter
        

out_file.close()