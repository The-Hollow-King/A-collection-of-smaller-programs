#Accepting and comparing three numbers and finding the greatest of them

#initializing three variables to accept the number from user
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))
if(num1 >= num2 and num1 >= num3) :
    print("Number 1 is the greatest number")
if(num2 >= num3 and num2 >= num1) :
    print("Number 2 is the greatest number")
if(num3 >= num1 and num3 >= num2) :
    print("Number 3 is the greatest number")
if(num1 == num2 == num3) :
    print("All the numbers are equal")
