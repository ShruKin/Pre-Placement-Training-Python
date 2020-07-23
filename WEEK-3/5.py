# 5. Write a python program to check if a user given string is a substring of another user
# given string or not

m = input("Enter the substring to be checked : ")
n = input("Enter the line : ")

if(n.count(m) > 0):
    print("'" + m + "' is a substring of given string")
else:
    print("'" + m + "' is NOT a substring of given string")
