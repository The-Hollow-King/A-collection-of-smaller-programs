#program to calculate the area of triangle, square and circle

#calculating area of a triangle
print("Calculating area of a triangle :-")
hei = float(input("Enter its height :"))#stores the value of height of the triangle
bas = float(input("Enter its base :"))#stores the value of base of the triangle
t_area = 0.5*bas*hei #calculates the area of the triangle
print("Area of the triangle is :", +t_area)

#calculating area of a square
print("Calculating area of a square :-")
len = float(input("Enter its length :"))#stores the value of the square's length
s_area = len*len #calculates the area of the square
print("Area of the square is :", +s_area)

#calculating area of a circle
print("Calculating area of a circle :-")
rad = float (input("Enter its radius :"))#stores the value of the circle's radius
pi = 3.14 #intializing pi's value
c_area = pi*rad*rad #calculates the area of the circle
print("Area of the circle is :", +c_area)
