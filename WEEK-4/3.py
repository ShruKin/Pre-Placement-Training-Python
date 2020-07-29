# List ‘X’ contains both positive and negative integers. Sort the list
# depending on the absolute values of the elements. The sorted list
# should have the actual initial values of the elements. Do not use
# function ‘sorted()’.

X = [-1, 23, 12, -9, -30, 2, 50, -50, 5, 30, 23, 50]

for i in range(len(X)):
    mi = i
    for j in range(i+1, len(X)):
        if abs(X[mi]) > abs(X[j]):
            mi = j

    X[i], X[mi] = X[mi], X[i]

print(X)
