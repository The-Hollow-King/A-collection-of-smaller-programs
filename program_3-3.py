#factorial of n number
print("Factorial program")
n = int(input("Enter the number you want the factorial of : "))
fac = 1
for i in range (1, n+1):
    fac = fac * i
print(fac)
