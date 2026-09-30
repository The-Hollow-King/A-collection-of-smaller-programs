#friend list
sch_f = input("Enter list of school friends with spaces: ")
sf_lst = sch_f.split()
print(sf_lst)

col_f = input("Enter list of college friends with spaces: ")
cf_lst = col_f.split()
print(cf_lst)

fr_lst = sf_lst + cf_lst
print("List of all friends :", fr_lst)
