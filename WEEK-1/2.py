# Print all the multiples of 3 and 5 from 1 to n

n = int(input("Enter the limit: "))

print("Multiples of 3 and 5: ")
for i in range(1, n+1):
    if(i % 3 == 0 and i % 5 == 0):
        print(i)
