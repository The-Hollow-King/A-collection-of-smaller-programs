#username checker
print("Welcome to the program")
print("Few rules for username \ni)Username can only cointain words \nii)Username cannot cointain spaces")
print("iii)Username cannot be more than 12 characters long")
user_n = input("Enter your username : ")
if len(user_n) > 12 :
    print("The username cannot exceed 12 characters")
elif not user_n.isalpha() :
    print("Username can only cointain words")
elif not user_n.find(" ") == -1 :
    print("Username cannot cointain spaces")
else :
    print("Welcome user!")
