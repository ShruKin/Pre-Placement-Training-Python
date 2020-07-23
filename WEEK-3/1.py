# 1. Write a python program to check if a user given string is Palindrome or not.

n = input("Enter a string: ")

if(n == n[::-1]):
    print("Its a palindrome string")
else:
    print("Its not a palindrome string")