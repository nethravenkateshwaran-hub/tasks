n=5

##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if j==3 or i==1 or (i==5 and j==1) or (i==5 and j==2):
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
##for i in range(1,n+1):
##   for j in range(1,n+1):
##       if i==1 or j=1:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()


"""s=input("enter name")
c=0
for i in s:
    print(i)
    c+=1
print(c)"

"vowels="aeiouAEIOU"
v=c=0
for i in s:
    if i in vowels:
        v+=1
    else:
        c+=1
        
print("vowels is",s,"count:",v)
print("constant is",s,"count:",v)
print("constant in",s,"count:",c)"
"""
s=input("enter name")
rev=""
for i in s:
    rev=i+rev
print("reverse str is",rev)
l=len(s)
if l==0:
    print("str is empty")
else:
    print("str is not empty")
  
