# 7. Print the following pattern:
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print((str(i)+" ")*i)
