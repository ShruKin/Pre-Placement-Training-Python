# 4. Write a python program to find the words in a user given line having length at least 2

n = input("Enter the line: ").split()
print("Words with length atleast 2:")
for i in n:
    if(len(i) >= 2):
        print(i, end=" ")
