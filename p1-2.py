#!/usr/bin/python
import random
def letters(string):
 up_string=string.upper()
 up_letter=[]
 for i in range (len(string)):
     if up_string[i]==string[i] and string[i]!=' ':
         up_letter.append(string[i])
 return up_letter
def palindrome(string):
 lower_string=string.lower().replace(' ', '')
 reverce_lower_string=lower_string[::-1]
 if reverce_lower_string==lower_string: return 'palindrome'
 else: return 'isnt palindrome'
def find_letter(string_in, letter):
 splitted_string=string_in.split()
 string_out=[]
 for i in range(len(splitted_string)):
    if splitted_string[i].startswith(letter):
        string_out.append(splitted_string[i])
 return string_out
def mix_words(string_in):
 splitted_string=string_in.split(' ')
 random.shuffle(splitted_string)
 joined_string=' '.join(splitted_string)
 string_out=joined_string.capitalize()
 return string_out
print letters("Trees Are So Kind")
print palindrome("A roza upala na lapu Azora")
print find_letter("Bears are the best animals ever", 'a')
print mix_words("Bears are the best animals ever")
