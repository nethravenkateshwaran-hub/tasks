##def even(a):
##    s=0
##    r=0
##    while a>0:
##        r=a%10
##        s+=r
##        a=a//10
##        print("sum of digits",s)
##even(26)
def count():
    c=0
    a=int(input("enter num"))
    while a>0:
        a=a//10
        c+=1
        print(c)

count()



            
    
