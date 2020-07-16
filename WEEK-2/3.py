# 3. Check whether a number is a palindrome

n = input("Enter a number: ")

if(n == n[::-1]):
    print("Its a palindrome number")
else:
    print("Its not a palindrome number")
