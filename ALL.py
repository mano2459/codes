# 1WAP TO ENTER A STRING AND CHECK WETHER THE STRING IS PALINDROME OR NOT USING WHILE LOOP.

str = input ("enter a string:-")
l = len (str)
p=1-1
index=0
while(index<p) :
    if(str[index]== str[p]):
        index = index +1
        p=p-1

    else:
            print("string is not a palindrome")

            break
else:
    print("string is a palindrome ")





'''#2WAP to count the number of alphabets , digits , uppercase, lowercase ,spaces




line = input("Enter the line:-")
lowercount=uppercount=0
alphacount=digitcount=alnumcount=spacecount=symcount=0             

for i in line :
    if i.islower():
        lowercount+=1
    if i.isupper():
        uppercount+=1
    if i.isalpha():
        alphacount+=1
    if i.isdigit():
        digitcount+=1
    if i.isalnum():
        alnumcount+=1
    if i.isspace():
        spacecount+=1
    if i.isalnum()!= True and i!= "" :
        symcount +=1


print ("Number of small letters :-" , lowercount)
print ("Number of capital letters :-" ,uppercount)
print ("Number of no of alphabet letters :-" , alphacount)
print ("Number of no of digit letters :-" , digitcount)
print ("Number of alphanumeric letters :-" , alnumcount)
print ("Number of space letters :-" , spacecount)
print ("Number of symbol letters :-" , symcount)'''


'''#3WAP TO REMOVE ALL ODD NUMBERS FROM THE GIVEN LIST.

list =[ 1, 2 ,3, 4, 5 , 6 ,7]
for i in list:
    if i% 2!=0:
       list.remove(i)
       print (list)'''


'''#4WAP TO DISPLAY THOSE STRING WHICH STARTS WITH A.
str="arnav ,vivek , aryan ,abc"
lst=str.split()
for a in lst:
    if a.startswith("a"):
         print(a)'''

'''#5WAP to sort the the unsorted list using for loop.
uns=[11,32,10,20,30,80]
print("the unsorted list is ",uns)
i=0
for i in range (len(uns)):
    for j in range (i,len(uns)):
        if uns[i]>uns[j]:
            uns[i],uns[j]= uns[j],uns[i]
            print("the list after sorting in loop" ,"is",uns)
            print("the sorted list ",uns)'''



'''

#6WAP TO INPUT THE TOTEL NUMBER OF SECTION IN CLASS 12TH AND DISPLAY ON THE OUTPUT SCREEN .
class12th={}
a=int(input("enter the no. of sections "))
for i in range(a):
    b = input("enter the section no.: ")
    c = input("enter the stream name.: ")
    class12th[b]=c

print ("class\t\t","section \t","stream name")
    
for j in class12th:
    print("12th","\t\t",j,"\t\t",class12th[j])
'''

 



'''#7WAP TO ENTER THE SINGLE ELEMENTS IN AN EMPTY TUPLE.
t = ()
a = int (input("enter the element:"))
t+= a,
print (t)'''

'''# 8WAP TO ENTER THE MULTIPLE
#  ELEMENT IN AN EMPTY TUPLE.
t = ()
n = int(input("enter the number of elements you want to\
     enter:"))
for i in range(n):
    a = int(input("enter the elements :"))
    t += a,
    print(t)
'''

'''#9WAP TO ENTER THE FACTORIAL OF A NUMBER USING FUNCTION.

def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)
    x = int (input("enter the number :"))
    p = fact(x)
    print(p)
z=fact(3)
print(z)'''

    




    
'''#10WAP TO INPUT TOTAL NO. OF SECTION PRINT SECTION NAME , NOW MANY SECTION , STREAM NAME , DISPLAY ALL.
d ={}
a = int(input("enter the no. of section in class 12th:")) 
for i in range (a):
    b = int(input("enter the section name :"))
    c = input("enter the stream name:")
    d[b]=c
    print (d)'''


'''#11WAP A PROGRAM TO INPUT THE NAME OF N COUNTRIES AND THEIR CAPITAL,CURRENCY AND DISPLAY IN A TABULAR FORM.
d={}
e=int(input("Enter the number of counrties:"))
i=1
while i<=e:
    co=input("enter the country name:")
    cap=input("Enter the capital name :")
    curre=input("enter the currency name:")
    d[co]=[cap,curre]
    i+=1
l=d.keys()
print("\ncountry\t\t","capital\t","currency")
for i in l:
   z=d[i]
   print(i,"\t\t",end=" ")
   for j in z:
       print (j,"\t\t",end=" ")'''



       
'''#12WAP TO READ DATA FROM A TEXT FILE DATA TEXT AND DISPLAY WORD WHICH HAVE MAXIMUM AND NMINIMUM CHARACTER.
f=open("DATA.txt")
s=f.read()
print(s)
words=s.split()
print(words,len(words))
max_ch=len(words[0])
finalmax=" "
for word in words:
    length=len(word)
    if max_ch<length:
        max_ch=length
        finalmax=word
    print("max word:",finalmax,"max_ch:",max_ch)'''


'''#13AP TO WRITE A STRING IN A BINARY FILE COMP.DAT AND COUNT THE NUMBER OF TIME A CHARACTER APPEAR A GIVEN STRING USING A DICTONARY.
    
import pickle
str1="this is the computer science with python "
f1=open("comp1.dat","wb+")
pickle.dump(str1,f1)
f1.close()
f1=open("comp1.dat","rb+")
a=pickle.load(f1)
print("the string is written in the",a)
f1.close()'''



'''#14
import pickle
f1=open("comp.dat","rb")
str=pickle.load(f1)
print("\n\nthe string in the binary file is :\n",str)
d={}
for i in str:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print("\n the occurence of each letter of string is:\n",d)
f1.close()'''

'''#15WAP to read the data from text file text and display each world with vowel and consonents
f=open("DATA.txt")
s=f.read()
print(s)
words=s.split()
print(words,len(words))
countv=0
countc=0
for word in words:
    for ch in word :
        if ch=='a' or ch=='e' or ch=='i'or ch=='o' or ch=='u':
            countv+=1
        else:
           countc+=1


print("word:",word,"v:",countv,"c:",countc)'''





