#program for filtering
import numpy as np

ages = np.array([[17,17,18,18,50,28,65,60],[15,14,16,18,19,25,43,68]])

teen = ages[ages<18]
# adults = ages[(ages >= 18) & (ages<60)]
# seniors = ages[ages>=60]
evens = ages[ages%2 == 0]
odds = ages[ages %2 != 0]

print(teen)
# print(adults)
# print(seniors)
print(evens)
print(odds)

#where function
adults = np.where(ages>=18, ages, np.nan)
print(adults)