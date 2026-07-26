#Election eligibility test program

#creating a variable to accept the users age
user_age = int(input("Enter you age(only integer):"))
if(user_age >= 18 and user_age <= 150):
    print("User is eligible to vote!")
elif(user_age < 18 and user_age >= 0) :
    print("User isn't eligibile to vote :(")
else :
    print("Invalid age")

