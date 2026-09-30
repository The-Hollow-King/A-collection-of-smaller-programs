#car list
n = int(input("How many cars do you want to add? "))
car_lst = []
for i in range(0,n):
     car = input(f"Enter car {i+1}: ")
     car_lst.append(car)
print(car_lst)
a = len(car_lst[0])
print("length of first element : ", +a)

print("Enter two more car names - ")
for i in range(2) :
    a = input(f"Car no.{i+1} : ")
    car_lst.append(a)
print(car_lst)

#to find the occurence
a = input("Enter the name you want to find out the occurence of : ") 
print("The occurence of the required car : ", car_lst.count(a))

#printing the 6th and 8th element
print("The 6th element : ", car_lst[5])
print("The 8th element : ", car_lst[7])

#remove any element
o = (input("Enter the position number of element u want to remove : "))
car_lst.remove(o)
print(car_lst)
