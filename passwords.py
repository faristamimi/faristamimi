password = input("enter your password: ")
length=len(password)
if length<10 or length>20:
    raise ValueError("password has to be between 10 and 20 characters")
confpass=input("confirm your password")
if password!=confpass:
    raise ValueError("passwords must match")
print(password)
