# 2. Write a python program to take Firstname and lastname as input.
# Check whether the first letter of both strings are in uppercase or not.
# If not change accordingly and print reformatted string.

fn = input('Firstname: ')
ln = input('Lastname: ')

if not fn[0].isupper():
    fn = fn.title()

if not ln[0].isupper():
    ln = ln.title()

print(fn + " " + ln)