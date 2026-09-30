#program to implement tuple in python

#a tuple to save the mobile nodel name accepted from the user
lstmob = []
print("Enter names of mobile companies(type quit to end)")
while True :
    item = input("> ")
    if item.lower() == "quit" :
        break
    lstmob.append(item)
mobtup = tuple(lstmob)
print("Names of the companies you entered : ", mobtup)

#length and index of an element in a tuple
idx1 = mobtup.index('Samsung')
len1 = len(mobtup[idx1])
print("The index number and length of 'Samsung' : ", idx1, ",", len1)

#concatenate two tuples
mobtup1 = ("itel", "Nokia", "Lava")
print("An old, previous tuple cointaining lists of mobile phone companies : ", mobtup1)
new_tup = mobtup1 + mobtup
print("New list : ", new_tup)

