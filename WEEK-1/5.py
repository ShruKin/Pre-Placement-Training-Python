# Print the sum of digits of a number

n = input("Enter a number: ")
s = sum(list(map(int, list(n))))
print("Sum of digits of is ", s)