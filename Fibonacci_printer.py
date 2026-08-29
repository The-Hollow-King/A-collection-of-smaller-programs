#print fibonnaci sequence till nth term
print("Fibonacci program")
n = int(input("Enter a number till which u want the fibonacci sequence till : "))
fib = 0
fib_1 = 1
for i in range (1,n+1):
    fib, fib_1 = fib_1, fib + fib_1
print(fib)
