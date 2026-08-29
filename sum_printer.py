#print sum of n numbers
n = int(input("enter an integer till which u want the sum of, starting from 1 : "))
sumn = 0
for i in range(1,n+1) :
    sumn = i + sumn
print (sumn)
