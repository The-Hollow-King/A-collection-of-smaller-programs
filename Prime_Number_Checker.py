#prime number checker
print("Welcome to the prime number checker!")
num = int(input("Enter the number you want to check (should be an integer) :"))
if (num %2 ==0):
    print("The entered number is not a prime number")
else :
    if (num % 3 == 0) :
        print("The entered number is a prime number!")
    else :
        print("The entered number is not a prime number")
