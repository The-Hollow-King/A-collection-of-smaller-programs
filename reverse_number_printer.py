#accept an integer and print its reverse
n = int(input("Enter a number to be reversed : "))
r_n = 0 #reversed number
n_str = str(n) #converting the variable into string data type
n_l = len(n_str) #length of the number 
for i in range(1, n_l+1) :
    d = n % 10 #unit digit
    r_n = (r_n*10) + d #adding the unit to the everse integer as its unit digit
    n = n // 10 #removing the final digit of the orignal number
print (r_n)
