#dice roller program
import random
print("Welcome to dice roller program!")
print("The program will go on for 5 rounds")
d_s = input("Enter (start) to roll a dice : ")
i = 0
while i < 5 :
    if d_s == "start":
        r = random.randint(1,6)
        print("The answer by the holy dice : ", +r)
    else :
        print("Invalid input")
    i = i + 1
    

