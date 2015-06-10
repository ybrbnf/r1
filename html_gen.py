#!/usr/bin/python
#coding: utf-8
class Tree:
    def __init__(self, tag1, tag2=None, tag3=None):
        self.tag1=tag1
        self.tag2=tag2
        self.tag3=tag3

    def __str__(self):
        return str(self.tag1)

in_file='in.txt'#исходный файл
out_file='out.html'#конечный файл
open_tags=[]#список открывающах тегов
close_tags=[]#список закравающ тегов

with open(in_file, 'r') as read_file:# пишем теги из файла в списки 
    for line in read_file:
        open_tags.append(line.strip('\n'))
        close_tags.append('/'+line.strip('\n'))

tree_open_tag=Tree(open_tags[0], Tree(open_tags[1]), Tree(open_tags[2]))
tree_close_tag=Tree(close_tags[0], Tree(close_tags[1]), Tree(close_tags[2]))

def print_tree_open(tree_open_tag, space=0): # расставляем открывашки с отступом
    if tree_open_tag==None: return
    print ' '*space+'<'+str(tree_open_tag.tag1)+'>'
    print_tree_open(tree_open_tag.tag2, space+1)
    print_tree_open(tree_open_tag.tag3, space+2)

def print_tree_close(tree_close_tag, space=0): #расставляем закрывашки с отступом
    if tree_close_tag==None: return
    print_tree_close(tree_close_tag.tag3, space+2) 
    print_tree_close(tree_close_tag.tag2, space+1)    
    print ' '*space+'<'+str(tree_close_tag.tag1)+'>'   
print_tree_open(tree_open_tag)
print_tree_close(tree_close_tag)

#with open(out_file, 'a') as save_file:
#    save_file.write()
#    save_file.write()
