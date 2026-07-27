#Simple interest calculator

p = int(input("Enter principal amount :")) #To accept the value of principal amount
n = float(input("Enter time period (in years) :")) #To accept the value of time period
r = float(input("Enter the rate :")) #To accept the value of rate

#formulae
si = (p*n*r)/100 #To calculate the amount of simple interest

#output
print("The amount of simple interest to be paid is :", +si)
