# 3. Write a python program to count the number of occurrences of a user given character in a user given string
#  within a user given index range.

para = input('Enter the string: ')
c = input('Enter character to search: ')
u, l = list(map(int, input('Enter range: ').split()))

print('Count:', para[u:l+1].count(c))
