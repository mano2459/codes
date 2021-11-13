


#program to count number of alphabets,digits,uppercase,lowercase,spaces and symbols of entered a line by the user




line=input("Enter the line:-")
lowercount=uppercount=0
alphacount=digitcount=alnumcount=spacecount=symcount=0
for i in line:
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
    if i.isalnum()!=True and i !="":
        symcount+=1
print("Number of small letters:-",lowercount)
print("Number of capital letters:-",uppercount)
print("Number of alphabet letters:-",alphacount)
print("Number of digits :-",digitcount)
print("Number of alphanumeric letters:-",alphacount)
print("Number of  spaces:-",spacecount)
print("Number of  symbols:-",symcount)



