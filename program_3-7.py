#pass checker
user_n = "ADMIN"
pas = 45678
i = 1
while i<=3 :
    in_user_n = input("Enter username : ")
    in_pas = input("Enter password : ")
    if in_user_n == user_n and pas == in_pas :
        print("Welcome admin!")
        end()
    else :
        print("Invalid username or password")
    i = i+1
