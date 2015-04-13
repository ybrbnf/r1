#!/usr/bin/python
import random

def letters(s):
 up=s.upper()
 q=[]
 for i in range (len(s)):
     if up[i]==s[i] and s[i]!=' ':
         q.append(s[i])
 return q
 
def palindrome(s):
 l=s.lower().replace(' ', '')
 w=l[::-1]
 if w==l: return 'palindrome'
 else: return 'isnt palindrome'

def find_letter(s, letter):
 l=s.split()
 d=[]
 for i in range(len(l)):
    if l[i].startswith(letter):
        d.append(l[i])
 return d

def mix_words(s):
 w=s.split(' ')
 random.shuffle(w)
 q=' '.join(w)
 e=q.capitalize()
 return e


print letters("Trees Are So Kind")

print palindrome("A roza upala na lapu Azora")

print find_letter("Bears are the best animals ever", 'a')

print mix_words("Bears are the best animals ever")
