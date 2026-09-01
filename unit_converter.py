#unit converter
print("Welcome to unit converter program!")
un = input("Input the unit of your orignal value (kms, miles, kg, lbs, cm, inches) : ")
va = float(input("Enter the value : "))
match un :
    case "kms" :
        va = va / 1.6
        print("Value in miles :", +va)
    case "miles" :
        va = va * 1.6
        print("Value in kms :", +va)
    case "kg" :
        va = va * 2.2
        print("Value in kg :", +va)
    case "lbs" :
        va = va / 2.2
        print("Value in lbs :", +va)
    case "cm" :
        va = va / 0.4
        print("Value in cm :", +va)
    case "inches" :
        va = va * 0.4
        print("Value in inches :", +va)
    case _ :
        print("Invalid unit")
        
