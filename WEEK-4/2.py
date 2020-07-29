# Find the K-th largest number in a list. ‘K’ is user given. You can use list already defined in program.

arr = [1, 23, 12, 9, 30, 2, 50, 50, 5, 30, 23, 50]
k = int(input("Enter k: "))

v = sorted(list(set(arr)))[-k]
print(f"The {k}-th largest no. is", v)
