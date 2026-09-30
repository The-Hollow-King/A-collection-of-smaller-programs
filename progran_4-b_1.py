flow = ["lily", "hibiscus", "lavender", "jasmine", "rose"]
print("List of flowers : ", flow)

print("First flower : ", flow[0])
print("Second flower : ", flow[1])

for flr in flow :
    print(flr)

flow.append("sunflower")
print("After appending : ", flow)

flow.insert(3,"tulip")
print("After insert : ", flow)

flow.remove(5)
print("After removing a value : ", flow)

try :
    flow.del()
    print(flow)
except :
    print("the list doesn't exist anymore")
