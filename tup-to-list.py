fruitstup = ("Apple", "Mango", "Custard apple", "Pappaya")

for fruit in fruitstup:
    print("Fruits = ", fruit)

print("Converting to list append data at last")
lstfruits = list(fruitstup)

print("type of fruitstup : ", type(fruitstup))
print("type of lstfruits : ", type(lstfruits))

#now we gist list now we can append, update, delete
len1 = len(fruitstup)
print("Length = ", len1)

#appending
lstfruits[len1-1] = "Gauva"
lstfruits.append("Gauva")
print("type of lstfruits ", lstfruits)

#update
lstfruits[3] = "Banana"
print("After updating lstfruits :", lstfruits)

lstfruits.insert(5, "Watermelon")
print("after insert in 5th index lstfruits : ", lstfruits)

#delete using index
del lstfruits[3]
print("After deleting 3rd data lstfruits : ", lstfruits)

#delete using index
lstfruits.remove("Watermelon")
print("after deleting 3rd data lstfruits : ", lstfruits)

#converting list back to tuple
fruitstup = tuple(lstfruits)
print("Tuple is : ", fruitstup)
print("Type of fruitstup : ", type(fruitstup))
print("Type of lstfruits : ", type(lstfruits))
