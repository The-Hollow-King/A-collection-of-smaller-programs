#To calculate the gross salary of an employee
print("SALARY PROGRAM")
name = input("Enter name of the employee :")
bs = float(input("Enter the basic salary :")) #to obtain value of basic salary

#other additional benefits
DA = (25/100)*bs
HRA = (15/100)*bs
PF = (12/100)*bs
TA = (7.50/100)*bs
net_sal = bs + DA + HRA + TA
gross_sal = net_sal - PF

#output
print("SALARY DETAILES")
print("=============================================")
print("NAME OF THE EMPLOYEE :", name)
print("BASIC SALARY :", +bs)
print("DEARNESS ALLOWANCE :", +DA)
print("HOUSE RENT ALLOWANCE :", +HRA)
print("TRAVEL ALLOWANCE :", +TA)
print("=============================================")
print("NET SALARY PAY :", +net_sal)
print("PROVIDENT FUND :", +PF)
print("=============================================")
print("GROSS PAYMENT :", +gross_sal)
