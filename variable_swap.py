#program to swap value of two variables with and without using temporary variable

#swaping values with temporary variable first
#accepting values from the user
print("Swapping values with temporary varible first")
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

#performing the swap now
temp = num1
num1 = num2
num2 = temp

#printing the output
print("The variables after swapping:")
print("Value of the first number :", +num1)
print("Value of the second number :", +num2)

#swaping values without temporary variable now
#accepting values from the user
print("Swapping values without temporary varible now")
num3 = int(input("Enter the third number :"))
num4 = int(input("Enter the fourth number :"))

#performing the swap now
num3,num4 = num4,num3

#printing the output
print("The variables after swapping:")
print("Value of the third number :", +num3)
print("Value of the fourth number :", +num4)
