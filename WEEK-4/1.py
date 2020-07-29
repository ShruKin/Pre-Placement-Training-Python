# List ‘X’ contains natural numbers with repetition. 
# Write a Python program to create a new list with only unique elements of ‘X’. 
# The program should not use any other collection except Lists.

X = []
ul = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    X.append(int(input()))
for j in X:
    if j not in ul:
        ul.append(j)
print("unique list :- ")
print(ul)
