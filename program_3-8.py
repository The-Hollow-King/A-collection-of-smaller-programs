#palindrome checker
print("Palindrome checker")
s = input("Enter a string")
i,j = 1, len(s)
cond = True

while i<j :
    if s[i] != s[j]:
        cond = False
        break
    i += 1
    j -= 1
if cond :
    print("Yes")
else :
    print("No")
