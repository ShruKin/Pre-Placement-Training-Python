# Write a program to print Fibonacci Series

n = int(input("Enter the limit: "))
a = 0
b = 1

print("The Fibonacci series is: ")
if n < 1:
    print(a)
else:
    print(a, b, end=" ")
    c = a + b
    while(c <= n):
        print(c, end=" ")
        a = b
        b = c
        c = a+b
