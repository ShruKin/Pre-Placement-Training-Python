# 5. Do the summation of the following series:
# 1 + 1/2 + 1/3 + ... + 1/n

n = int(input("Enter n: "))

s = sum([1/x for x in range(1, n+1)])
print(s)