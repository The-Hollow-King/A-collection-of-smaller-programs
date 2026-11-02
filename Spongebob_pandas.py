import pandas as ps

dic = {'Name' : ['Spongebob', 'Patrick', 'Squidward'], 'Ages' : [20, 20, 35], 'Jobs' : ['Cook', 'expert in the "art of doing nothing".', 'Cashier']}
var = ps.DataFrame(dic, index=["Friend 1", "Friend 2", "Friend 3"])

var["Money"] = [200,50,500]

add_dic = ps.DataFrame([{'Name' : 'Sandy', 'Ages' : 25, 'Jobs' : 'Engineer', 'Money' : 1000}, {'Name' : 'Eugene', 'Ages' : 60, 'Jobs' : 'Manager', 'Money' : 50000}], index = ['Acquaintance 1', 'Acquaintance 2'])
var = ps.concat([var,add_dic])
print(var)