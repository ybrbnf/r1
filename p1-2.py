#!/usr/bin/python

def letters(S):
 U=S.upper()
 Q=''
 for i in range (len(S)):
     if U[i]==S[i]:
         Q=Q+S[i]
 return Q
 
def palindrome(S):
 L=S.lower()
 L=L.replace(' ', '')
 W=''
 for i in range(len(S)):
     W=W+(S[len(S)-1-i])
 if W==S:
      return ('palindrome')
 else: return 'isnt palindrome'
def find_letter(S, letter):
 words=''
 def slovo(p, x):
  l=''
  while S[x]!=p:
      l=l+S[x]
      x+=1
  return l
 if S[0]==letter:
     slovo(' ', 0)
     words=words+slovo(' ',0)+' '
 for i in range(1, len(S)):
     if S[i] == letter and S[i-1] == ' ':
         words=words+slovo(' ',i)+' '
 return (words)

def mix_words(S):
 import random
 W=S.split(' ')
 random.shuffle(W)
 q=' '.join(W)
 Q=q.capitalize()
 return Q


print letters("Trees Are So Kind")

print palindrome("avi diva")

print find_letter("Bears are the best animals ever", 'B')

print mix_words("Bears are the best animals ever")
