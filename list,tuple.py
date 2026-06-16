##s=input("entera name")
##c=0
##for i in s:
##        print(i)
##        c+=1
##        print(c)

##vowel="aeiouAEIOU"
##v=c=0
##for i in s:
##    if i in vowel:
##        v+=1
##    else:
##        c+=1
##        
##print("vowels is",s,"count",v)
##print("constant in",s,"count",v)
##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or j==1 or i==3 :
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
####    print()
##
##a={1,2,3,4,5}
##b={2,4,5,6,7,8}
####print(a.union(b))
##print(a.intersection(b))
##a.intersection_update(b)
##print(a)
##print(a.difference(b))

#tuple
##a=(1,2,3,4,5)
##a+=(6,)
##print(a)
##c=0
##for i in a:
##    c+=1
##print(c)
##b=a[::-1]
##print(b)
##s=input("enter the name")
##r=" "
##for i in s:
##    if i!=" ":
##        r+=i
##print(r)
'''n=5
for i in range(n):

   print(" "*(n-i-1),end=" ")

   for j in range(i+1):
        print(chr(65+j),end=" ")
        
   for k in range(i-1,-1,-1):
       print(chr(65+j) ,end=" ")
       
   print()
   
for i in range(n,-2,-1,-1):
    
    print(" "*(n-i-1),end=" ")

    for j in range(i+1):
       print(chr(65+j),end=" ")
       
    for k in range(i,-1,-1,-1):
        print(chr(65+j),end=" ")
        
    print()'''

n=5

for i in range(1,n+1):
    
    print("*" * i,end="")
    
    print(" " * (2*(n-i)),end="")
   
    print("*" * i)
   
for i in range(n,0,-1):
    
    print("*" * i,end="")
    
    print(" " * (2*(n-i)),end="")
    
    print("*" * i)
    
    




















   
    
