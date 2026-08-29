#multiplcation table using while loop
n = int(input("Enter the number whose multiplication table you want : "))
sum = 1
i=1
while i <=10 :
    sum = n * i
    print(n, "*", i, "=", sum)
    i = i+1
