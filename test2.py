def function():
    password=input("enter a char")
if
    if len(password) == 8:
        print("Password length must be 8 characters")
    else:
         print("Password length its not 8 characters")       
    if any(ch.isupper() for ch in password):
        print("Password has an uppercase letter")
    else:
        print("Password has no uppercase letter")       
       
    if any(ch.islower() for ch in password):
        print("Password has a lowercase letter")
            
    else:
        print("Password it has no lowercase letter")
    if password=="@#$%^&*!":
        print("Password has  a special character")
    else:
        print("Password it has no a special character")
    if any (ch.isalnum() for ch in password):
        print("Valid Password")      
else:
    print("InValid Password")

function()
