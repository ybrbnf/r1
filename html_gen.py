#!/usr/bin/python
#coding: utf-8

class Tree:
    def __init__(self, data=None, level=None):
        self.data=data
        self.level=level

    def __str__(self):
        return str(self.data)
        

open_tags=[]#список открывающах тегов
close_tags=[]#список закравающ тегов
tmp=[] #временный список
level=0
        
print ('Программа генерирует HTML файл (out.html) исходя из тегов, записанных построчно в исходном файле (in.txt)')
try:
    in_file=open('in.txt', 'r')
except IOError:
    print "Исходный файл не найден. Программа будет завершена."
else:
# пишем теги из файла в списки 
    for line in in_file:
        open_tags.append(line.strip('\n'))
        tmp.append('/'+line.strip('\n'))
    close_tags=tmp[::-1]
    out_file=open('out.html', 'w')

# строим дерево открывающих тегов
    for elem in open_tags:
        data=elem
        node=Tree(data, level)
        out_file.writelines (' '*level+'<'+str(node)+'>\n')
        level+=1
    level-=1

# строим дерево закрывающих тегов
    for elem in close_tags:
        data=elem
        node=Tree(data, level)
        out_file.writelines (' '*level+'<'+str(node)+'>\n')
        level-=1
    print "Исходный файл обработан. Итоговый файл {}".format(out_file.name)