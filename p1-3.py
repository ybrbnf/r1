#!/usr/bin/python
#1-3-1
def l1(lst_in):
 print '-----------------1-3-1----------' 
 lst_out=[]
 lst_x=[]
 for elem in lst_in: 
     counter=lst_in.count(elem)
     if counter>=2:
         lst_x.append(elem)
 for elem in lst_x:
    if elem not in lst_out:
        lst_out.append(elem)
 return lst_out
#1-3-2
def l2(*arg):
 print '-----------------1-3-2----------'
 lst_out=[]
 lst=[]
 for j in arg:
    lst_out.append(type(j))    
    count_arg=lst_out.count(type(j))
    type_arg=type(j)
    print type_arg,'=>',count_arg
 return lst
#1-3-3
def last_chars (*arg):
 for word in arg:
  return word[len(word)-1:]
def l3(*arg):
 print '-----------------1-3-3----------'
 lst_out=[]
 for word in arg:
    lst_out.append(word)
 lst_out.sort(key=last_chars)
 return lst_out
#1-3-4
def l4(lst,string):
 print '-----------------1-3-4----------'     
 index=0
 for arg in lst:
     if string>arg:
         index+=1
 lst.insert(index,string)
 return lst
#1-3-5
def l5(lst1,lst2,x):	
 print '-----------------1-3-5----------'
 lst2.insert(lst1.index(x),x)
 return lst2
#1-3-6
def s6(lst_in):
 print '-----------------1-3-6----------'
 lst_x=lst_in.split()
 lst_out=[]
 for elem in lst_x:
     if len(elem)%2==0:
         lst_out.append(elem)
 return lst_out
#1-3-7
def l7(lst_in):
 print '-----------------1-3-7----------'
 count_max = count = 1
 for i in range(len(lst_in)):
     if lst_in[i]-lst_in[i-1]==1:
         count+=1
     else:
         if count>count_max:
             count_max=count
         count=1
 if count>count_max:
     count_max=count
 count=1
 for i in range(1,len(lst_in)):
     if lst_in[i]-lst_in[i-1]==1:
         count+=1
         if count==count_max:
             return lst_in[i-count_max+1:i+1]
     else: count=1 
print l1(['aso','liy','aso','gug','sdolf','liy'])
print l2(('sdgfd','asdfs'),'asa', 4, ['gu sdb'], {1:1, 2:2}, ('sdgfd','asdfs'))
print l3('klsdhgfkz','asa','rliyd','gusdb','olfc')
print l4(['alfa','delta','yota'],'beta')
print l5(['asa','liyg','rrrr','gusdy'],['olfd','ldks','hrfkjhc'],'rrrr')
print s6('jkdlj kjfh zlkhf lfoelc')
print l7([1, 2, 3, 5, 7, 8, 9, 10, 11, 12])
