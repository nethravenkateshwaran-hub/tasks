##a=int(input("enter a num"))
##b=int(input("enter a num"))
##a,b=b,a
##print("a",a)
##print("b",b)

##a=int(input("enter a no"))
##t=a
##s=0
##c=0
##while a>0:
##   a=a//10
##   s+=1
##while t>0:
##    r=t%10
##    c=c+r**s
##    t=t//10
##    print("rem is",c)
##    print("arm value",c)
##    print("update",t)

##n=5
##for i in range(1,n+1):
## print("*"*i,end="")
## print(" "*(2*(n-i)),end="")
## print("*"*i)
##for i in range(n,0,-1):
## print("*"*i,end="")
## print(" "*(2*(n-i)),end="")
## print("*"*i)
##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or j==3 or i==5:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
##
##
##s=input("enter name")
##vowle="aeiouAEIOU"
##v=c=0
##for i in s:
##    if i in vowle:
##        v+=1
##else:
##    c+=1
##    print("vowle is",s,"count:",v)
##    print("constant in",s,"count:",c)


##a=int(input ("enter the num"))
##for i in range(1,a+1):
##    if a%i==0:
##      print(i)
##s=input("enter name")
##r=" "
##c=0
##k=0
##for i in s:
##    c=ord(i)
##    if c>=97 and c<=122:
##        k=C-32
##        re=chr(k)
##        r+=re
##        print(r)
##    else:
##        r+=i
##        print(r)
    
      
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(prime(7))

    
    





































##
##s=input("enter a name")
##rev=""
##for i in s:
##    rev=i+rev
##if s==rev:
##    print("palindrome")
##else:
##    print("not a palindrome")
####
##
##
##


##s=input("enter name")
##r=" "
##for i in s:
##    if i!=" ":
##        r+=i
##print(r)
##
























